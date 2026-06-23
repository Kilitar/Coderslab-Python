import os
import sys
import re
import json
import time
import requests
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup, NavigableString

# Reconfigure stdout to use UTF-8 on Windows console
if sys.platform.startswith("win"):
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

BASE_URL = "https://lms.coderslab.cz"
LMS_API = f"{BASE_URL}/lms-api"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"
INSTANCE_ID = "328"

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
JWT_TOKEN = None

WORKSPACE_ROOT = Path(r"x:\PROJECTS\coderslab-python")
DATA_DIR = WORKSPACE_ROOT / "DATA"
SESSION1_DIR = DATA_DIR / "SESSION1_EXERCISE"
SESSION2_DIR = DATA_DIR / "SESSION2_MATERIALS"

def login():
    global JWT_TOKEN
    try:
        r = session.get(f"{BASE_URL}/login")
        form = re.search(r'<form[^>]+action=["\']([^"\']+)["\']', r.text)
        post_url = urljoin(BASE_URL, form.group(1)) if form else f"{BASE_URL}/login_check"
        session.post(post_url, data={"_username": EMAIL, "_password": PASSWORD, "_rememberMe": "on"}, allow_redirects=True)
        for c in session.cookies:
            if c.name == "jwt":
                JWT_TOKEN = c.value
        print(f"[+] Login successful. JWT token: {'obtained' if JWT_TOKEN else 'MISSING'}")
        return bool(JWT_TOKEN)
    except Exception as e:
        print(f"[-] Login error: {e}")
        return False

def sanitize(name):
    name = re.sub(r'[\\/*?:"<>|]', "_", str(name)).strip(". ")
    return " ".join(name.split())[:100]

def clean_name(s):
    s = re.sub(r'^\d+[-_]?', '', s)
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s.lower())
    return " ".join(s.split())

def html_to_markdown(html):
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    
    def process_node(node):
        if isinstance(node, NavigableString):
            return node.string or ""
        
        tag = node.name
        if not tag:
            return ""
        
        children_text = "".join(process_node(child) for child in node.children)
        
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            return f"\n\n{'#' * level} {children_text.strip()}\n\n"
        elif tag == "p":
            return f"\n\n{children_text.strip()}\n\n"
        elif tag in ("strong", "b"):
            return f"**{children_text}**"
        elif tag in ("em", "i"):
            return f"*{children_text}*"
        elif tag == "code":
            if node.parent and node.parent.name == "pre":
                return children_text
            return f"`{children_text}`"
        elif tag == "pre":
            code_node = node.find("code")
            code_text = code_node.get_text() if code_node else children_text
            lang = ""
            if code_node and code_node.has_attr("class"):
                classes = code_node["class"]
                for c in classes:
                    if c.startswith("language-"):
                        lang = c.replace("language-", "")
            return f"\n``` {lang}\n{code_text.strip()}\n```\n"
        elif tag == "ul":
            li_texts = []
            for child in node.children:
                if child.name == "li":
                    txt = "".join(process_node(c) for c in child.children).strip()
                    txt = txt.replace("\n", "\n  ")
                    li_texts.append(f"- {txt}")
            return "\n" + "\n".join(li_texts) + "\n"
        elif tag == "ol":
            li_texts = []
            idx = 1
            for child in node.children:
                if child.name == "li":
                    txt = "".join(process_node(c) for c in child.children).strip()
                    txt = txt.replace("\n", "\n  ")
                    li_texts.append(f"{idx}. {txt}")
                    idx += 1
            return "\n" + "\n".join(li_texts) + "\n"
        elif tag == "li":
            return children_text
        elif tag == "a":
            href = node.get("href", "")
            return f"[{children_text}]({href})"
        elif tag == "blockquote":
            lines = [f"> {line}" for line in children_text.strip().split("\n")]
            return "\n\n" + "\n".join(lines) + "\n\n"
        elif tag == "br":
            return "\n"
        elif tag == "hr":
            return "\n\n---\n\n"
        elif tag == "img":
            alt = node.get("alt", "")
            src = node.get("src", "")
            return f"![{alt}]({src})"
        elif tag == "table":
            rows = []
            for tr in node.find_all("tr"):
                cells = [c.get_text().strip() for c in tr.find_all(["td", "th"])]
                rows.append("| " + " | ".join(cells) + " |")
            if not rows:
                return ""
            header_len = len(node.find("tr").find_all(["td", "th"]))
            separator = "| " + " | ".join(["---"] * header_len) + " |"
            rows.insert(1, separator)
            return "\n\n" + "\n".join(rows) + "\n\n"
        else:
            return children_text

    md = process_node(soup)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()

def get_chapter_base_dir(mod_key, ch_slug, ch_name):
    mod_num = int(mod_key.split("_")[1])
    clean_ch = clean_name(ch_name)
    
    # 1. Check if there's an existing directory in Session 1 or Session 2 that matches the chapter name
    for root in (SESSION1_DIR, SESSION2_DIR):
        if not root.exists():
            continue
        for child in root.iterdir():
            if child.is_dir():
                clean_child = clean_name(child.name)
                if clean_ch in clean_child or clean_child in clean_ch:
                    return child

    # 2. Fallbacks based on module number
    if mod_num == 0:
        return SESSION1_DIR / "00_Intro_DA_Prework" / sanitize(f"{ch_slug}_{ch_name}")
    elif mod_num == 1:
        if "day 1" in clean_ch:
            return SESSION1_DIR / "02_Day 1"
        elif "day 2" in clean_ch:
            return SESSION1_DIR / "03_Day 2"
        elif "homework" in clean_ch or "summary" in clean_ch:
            return SESSION1_DIR / "04_Summary"
        else:
            return SESSION1_DIR / sanitize(f"{ch_slug}_{ch_name}")
    elif mod_num == 2:
        return SESSION2_DIR / "01_SQL_Prework" / sanitize(f"{ch_slug}_{ch_name}")
    elif mod_num == 3:
        return SESSION2_DIR / "02_SQL_Classes" / sanitize(f"{ch_slug}_{ch_name}")
    elif mod_num == 4:
        return SESSION2_DIR / "00_Python_Prework" / sanitize(f"{ch_slug}_{ch_name}")
    elif mod_num == 5:
        if "day 1" in clean_ch:
            return SESSION1_DIR / "02_Day 1"
        elif "day 2" in clean_ch:
            return SESSION1_DIR / "03_Day 2"
        elif "day 3" in clean_ch:
            return SESSION2_DIR / "03_Day 3 - PostgreSQL"
        elif "day 4" in clean_ch:
            return SESSION2_DIR / "04_Day 4 - API"
        elif "day 5" in clean_ch:
            return SESSION2_DIR / "05_Day 5 - Pandas"
        elif "day 6" in clean_ch:
            return SESSION2_DIR / "06_Day 6 - Pandas cont"
        elif "day 7" in clean_ch:
            return SESSION2_DIR / "07_Day 7 - Plots"
        elif "day 8" in clean_ch:
            return SESSION2_DIR / "08_Day 8 - Web scraping"
        elif "day 9" in clean_ch:
            return SESSION2_DIR / "09_Day 9 - Generating PDF"
        elif "day 10" in clean_ch:
            return SESSION2_DIR / "10_Day 10 - Workshop"
        else:
            return SESSION2_DIR / sanitize(f"{ch_slug}_{ch_name}")

    return SESSION2_DIR / sanitize(f"{ch_slug}_{ch_name}")

def find_matching_notebook_in_dir(base_dir, mat_name):
    if not base_dir.exists():
        return None, None
        
    clean_mat = clean_name(mat_name)
    
    # Recursively check for .ipynb files inside base_dir
    for dirpath, _, filenames in os.walk(base_dir):
        for f in filenames:
            if f.endswith(".ipynb"):
                name_without_ext = Path(f).stem
                if clean_name(name_without_ext) == clean_mat:
                    return Path(dirpath), name_without_ext
                    
    # Try fuzzy match if exact cleaned name doesn't match
    for dirpath, _, filenames in os.walk(base_dir):
        for f in filenames:
            if f.endswith(".ipynb"):
                name_without_ext = Path(f).stem
                c_name = clean_name(name_without_ext)
                if clean_mat in c_name or c_name in clean_mat:
                    return Path(dirpath), name_without_ext
                    
    return None, None

def main():
    if not login():
        print("[-] Auth failed.")
        exit(1)
        
    map_path = WORKSPACE_ROOT / "course_materials_map.json"
    if not map_path.exists():
        print(f"[-] Course map not found at {map_path}")
        exit(1)
        
    with open(map_path, "r", encoding="utf-8") as f:
        course_map = json.load(f)
        
    total_saved = 0
    total_failed = 0
    total_skipped = 0
    
    for mod_key in sorted(course_map.keys()):
        mod_num = int(mod_key.split("_")[1])
        if mod_num > 5:
            continue
            
        mod_val = course_map[mod_key]
        print(f"\n[*] Processing module: {mod_val.get('name')}")
        chapters = mod_val.get("chapters", [])
        
        for ch in chapters:
            ch_slug = ch.get("slug")
            ch_name = ch.get("name")
            mats = ch.get("materials", [])
            
            print(f"  [*] Chapter {ch_slug}: {ch_name} ({len(mats)} materials)")
            
            # 1. Determine target directory for this chapter
            ch_base_dir = get_chapter_base_dir(mod_key, ch_slug, ch_name)
            
            for idx, m in enumerate(mats, start=1):
                m_type = m.get("type")
                m_name = m.get("name")
                m_id = m.get("id")
                
                if m_type not in ("article", "exercise", "presentation_reveal"):
                    total_skipped += 1
                    continue
                    
                print(f"    [*] Fetching [{m_type}] {m_name}...")
                
                # Fetch details
                url = f"{LMS_API}/material/{INSTANCE_ID}/{ch_slug}/{m_id}"
                try:
                    r = session.get(url, headers={"Authorization": f"Bearer {JWT_TOKEN}"}, timeout=15)
                    if r.status_code != 200:
                        print(f"      [ ] Failed to fetch (Status {r.status_code}). Skipping.")
                        total_failed += 1
                        continue
                        
                    res_data = r.json()
                    mat_data = res_data.get("data", {})
                    content_data = mat_data.get("content", {})
                    html = content_data.get("html", "")
                    
                    if not html:
                        print("      [ ] HTML content is empty. Skipping.")
                        total_skipped += 1
                        continue
                        
                    markdown_text = html_to_markdown(html)
                    
                    # 2. Search for matching notebook ONLY inside the chapter base directory
                    nb_dir, nb_name = find_matching_notebook_in_dir(ch_base_dir, m_name)
                    
                    if nb_dir:
                        dest_dir = nb_dir
                        filename = nb_name
                    else:
                        dest_dir = ch_base_dir
                        filename = f"{idx:02d}_{sanitize(m_name)}"
                        
                    dest_path = dest_dir / f"{filename}.md"
                    
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(dest_path, "w", encoding="utf-8") as out_f:
                        out_f.write(f"# {m_name}\n\nType: {m_type.capitalize()}\n\n{markdown_text}\n")
                        
                    print(f"      [+] Saved to: {dest_path.relative_to(WORKSPACE_ROOT)}")
                    total_saved += 1
                    
                    time.sleep(0.1)
                except Exception as ex:
                    print(f"      [-] Exception occurred: {ex}")
                    total_failed += 1
                    
    print(f"\n[+] Task completed!")
    print(f"    - Saved: {total_saved} Markdown files")
    print(f"    - Skipped: {total_skipped} non-content/empty materials")
    print(f"    - Failed: {total_failed} downloads")

if __name__ == "__main__":
    main()
