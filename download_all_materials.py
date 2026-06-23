import re
import json
import time
import requests
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://lms.coderslab.cz"
LMS_API = f"{BASE_URL}/lms-api"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"
INSTANCE_ID = "328"
DOWNLOAD_ROOT = Path("DATA") / "SESSION2_MATERIALS"

# Map module keys to clean directory prefixes
MODULE_DIR_MAP = {
    "module_0": "00_Prework",
    "module_1": "01_Intro_DA",
    "module_2": "02_SQL_Prework",
    "module_3": "03_SQL_Classes",
    "module_4": "04_Python_Prework",
    "module_5": "05_Python_Classes",
    "module_6": "06_Viz_Prework",
    "module_7": "07_Viz_Classes",
}

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
JWT_TOKEN = None

def login():
    global JWT_TOKEN
    r = session.get(f"{BASE_URL}/login")
    form = re.search(r'<form[^>]+action=["\']([^"\']+)["\']', r.text)
    post_url = urljoin(BASE_URL, form.group(1)) if form else f"{BASE_URL}/login_check"
    session.post(post_url, data={"_username": EMAIL, "_password": PASSWORD, "_rememberMe": "on"}, allow_redirects=True)
    for c in session.cookies:
        if c.name == "jwt":
            JWT_TOKEN = c.value
    print(f"[+] Login successful. JWT token: {'obtained' if JWT_TOKEN else 'MISSING'}")
    return bool(JWT_TOKEN)

def sanitize(name):
    return re.sub(r'[\\/*?:"<>|]', "_", str(name)).strip(". ")[:80]

def download_file(url, dest_dir, filename=None):
    try:
        r = session.get(url, headers={"Authorization": f"Bearer {JWT_TOKEN}"}, stream=True, timeout=60)
        r.raise_for_status()
        if not filename:
            cd = r.headers.get("Content-Disposition", "")
            m = re.search(r'filename[^;=\n]*=(["\']?)([^"\';\n]+)\1', cd)
            filename = m.group(2).strip() if m else sanitize(url.split("/")[-1].split("?")[0])
        
        # Ensure correct extension (like .zip, .ipynb, .pdf) if we can detect it
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / sanitize(filename)
        
        with open(dest, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        size = dest.stat().st_size
        print(f"    [+] DOWNLOADED: {dest.name} ({size//1024} KB)")
        return True
    except Exception as e:
        print(f"    [-] Error downloading {url}: {e}")
        return False

def main():
    if not login():
        exit(1)

    with open("course_materials_map.json", "r", encoding="utf-8") as f:
        course_map = json.load(f)

    total_downloaded = 0
    total_failed = 0

    for mod_key, mod_val in course_map.items():
        mod_prefix = MODULE_DIR_MAP.get(mod_key, mod_key)
        chapters = mod_val.get("chapters", [])
        
        for ch in chapters:
            slug = ch.get("slug")
            ch_name = sanitize(ch.get("name"))
            mats = ch.get("materials", [])
            
            # Destination folder format: 00_Prework/0-6_Downloadable_materials
            dest_dir = DOWNLOAD_ROOT / mod_prefix / f"{slug}_{ch_name}"
            
            for m in mats:
                mat_type = m.get("type")
                mat_name = m.get("name")
                mat_id = m.get("id")
                
                # Check if it's a downloadable type
                if mat_type in ("attachment", "file", "zip", "download"):
                    print(f"[*] Processing material: {mat_name} ({mat_type}) in {slug}")
                    content = m.get("content") or {}
                    
                    # Try to find a direct URL in content fields
                    dl_url = None
                    for key in ("url", "fileUrl", "file_url", "downloadUrl", "externalUrl", "src"):
                        val = content.get(key, "")
                        if val and any(ext in val.lower() for ext in [".zip", ".pdf", ".ipynb", ".py", ".csv", ".xlsx", ".rar", ".tar"]):
                            dl_url = urljoin(BASE_URL, val) if val.startswith("/") else val
                            break
                    
                    # Fallback to direct material download endpoint
                    if not dl_url:
                        dl_url = f"{LMS_API}/material/{INSTANCE_ID}/{slug}/{mat_id}/download"
                    
                    # Attempt download
                    success = download_file(dl_url, dest_dir, mat_name)
                    if success:
                        total_downloaded += 1
                    else:
                        total_failed += 1
                    
                    time.sleep(0.2) # Gentle delay between requests

    print(f"\n[+] Download completed! Successfully downloaded: {total_downloaded} files, Failed: {total_failed} files.")

if __name__ == "__main__":
    main()
