"""
Stahuje materialy z LMS.
Pouziva zname materialId a sleduje next/prev pro prochazeni kapitoly.
"""
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
DOWNLOAD_DIR = Path("DATA") / "SESSION2_MATERIALS"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

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
    print(f"[+] Login OK, JWT: {'ziskan' if JWT_TOKEN else 'CHYBI!'}")
    return bool(JWT_TOKEN)


def get_mat(slug, mat_id):
    url = f"{LMS_API}/material/{INSTANCE_ID}/{slug}/{mat_id}"
    r = session.get(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {JWT_TOKEN}",
    }, timeout=20)
    if r.status_code == 200 and "json" in r.headers.get("Content-Type", ""):
        return r.json().get("data")
    return None


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
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / sanitize(filename)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        size = dest.stat().st_size
        print(f"    [+] STAZENO: {dest.name} ({size//1024} KB)")
        return True
    except Exception as e:
        print(f"    [-] Chyba {url}: {e}")
        return False


def process_chapter(slug, start_id, dest_dir, chapter_name=""):
    """Traverse all materials in a chapter starting from start_id."""
    print(f"\n[*] Kapitola {slug}: {chapter_name}")
    visited = set()
    current_id = start_id
    downloaded = 0
    all_types = []

    while current_id and current_id not in visited:
        visited.add(current_id)
        mat = get_mat(slug, current_id)
        if not mat:
            print(f"  [!] Nelze nacist material {current_id[:8]}")
            break

        mat_type = mat.get("type", "unknown")
        mat_name = mat.get("name", current_id)
        content = mat.get("content", {}) or {}
        all_types.append(f"{mat_type}:{mat_name}")
        print(f"  [{mat_type}] {mat_name}")

        # Download if it's an attachment
        if mat_type in ("attachment", "file", "zip", "download"):
            for key in ("url", "fileUrl", "file_url", "downloadUrl", "externalUrl", "src"):
                val = content.get(key, "")
                if val and any(ext in val.lower() for ext in [".zip", ".pdf", ".ipynb", ".py", ".csv", ".xlsx", ".rar", ".tar"]):
                    full_url = urljoin(BASE_URL, val) if val.startswith("/") else val
                    if download_file(full_url, dest_dir, mat_name):
                        downloaded += 1
                    break
            else:
                # Try direct URL build
                dl_url = f"{LMS_API}/material/{INSTANCE_ID}/{slug}/{current_id}/download"
                r = session.get(dl_url, headers={"Authorization": f"Bearer {JWT_TOKEN}"}, timeout=10)
                if r.status_code == 200 and "json" not in r.headers.get("Content-Type", ""):
                    if download_file(dl_url, dest_dir, mat_name):
                        downloaded += 1

        # Also check if any content values look like files
        for key, val in content.items():
            if isinstance(val, str) and any(
                ext in val.lower() for ext in [".zip", ".pdf", ".xlsx", ".rar", ".tar.gz"]
            ) and ("http" in val or val.startswith("/")):
                full_url = urljoin(BASE_URL, val) if val.startswith("/") else val
                print(f"    -> Nalezen soubor ({key}): {val}")
                if download_file(full_url, dest_dir, f"{mat_name}_{key}"):
                    downloaded += 1

        # Follow next
        nxt = mat.get("next")
        if isinstance(nxt, dict):
            current_id = nxt.get("id")
        elif isinstance(nxt, str) and len(nxt) == 36:
            current_id = nxt
        else:
            current_id = None

        time.sleep(0.15)

    print(f"  Typy materialu: {', '.join(all_types)}")
    return downloaded


if not login():
    exit(1)

# Kapitoly s prilohy a jejich PRVNI material ID
# Formát: (slug, first_materialId, nazev, slozka)
# Zname:
# 0-6 -> dd28a343-5fdb-4525-8030-d680ca0ae9e8 (Downloadable materials session 1)
# Ostatni budeme pridat postupne

chapters = [
    ("0-6", "dd28a343-5fdb-4525-8030-d680ca0ae9e8", "Downloadable_materials_session1",
     DOWNLOAD_DIR / "00_Prework" / "session1_materials"),
    ("1-4", "4f7cd228-10a9-4b2f-97c8-64a866c60858", "Downloadable_materials_session2",
     DOWNLOAD_DIR / "01_Intro_DA" / "session2_materials"),
    ("5-8", "792279f7-0a41-44dc-b512-b6d16911faff", "Python_session3_prep",
     DOWNLOAD_DIR / "05_Python" / "session3_prep"),
]

total = 0
for slug, first_id, name, dest in chapters:
    n = process_chapter(slug, first_id, dest, name)
    total += n

print(f"\n[+] Hotovo! Celkem stazeno: {total} souboru")
print("\nSoubory v SESSION2_MATERIALS:")
for f in sorted(DOWNLOAD_DIR.rglob("*")):
    if f.is_file():
        print(f"  {f.relative_to(DOWNLOAD_DIR)} ({f.stat().st_size//1024} KB)")
