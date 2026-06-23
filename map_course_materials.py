import re
import json
import requests
from urllib.parse import urljoin

BASE_URL = "https://lms.coderslab.cz"
LMS_API = f"{BASE_URL}/lms-api"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
JWT_TOKEN = None

def login():
    global JWT_TOKEN
    r = session.get(f"{BASE_URL}/login")
    form = re.search(r'<form[^>]+action=["\']([^"\']+)["\']', r.text)
    post_url = urljoin(BASE_URL, form.group(1)) if form else f"{BASE_URL}/login_check"
    resp = session.post(post_url, data={"_username": EMAIL, "_password": PASSWORD, "_rememberMe": "on"}, allow_redirects=True)
    for c in session.cookies:
        if c.name == "jwt":
            JWT_TOKEN = c.value
    print(f"[+] Login successful. JWT token: {'obtained' if JWT_TOKEN else 'MISSING'}")
    return bool(JWT_TOKEN)

# We use one representative chapter ID per module to fetch the module menu:
chapter_ids = [
    "70240d28-0ed4-46b5-965b-e5d06c446fa6", # Module 0
    "c6c2172b-982b-442b-ad94-e436cf52619c", # Module 1
    "63116b4a-24d3-4394-a111-a1e4a413e552", # Module 2
    "af266dce-d1d2-4171-8093-0c5f8e8ee970", # Module 3
    "7dccf12d-38c8-4c70-b6ef-ee89b06ba179", # Module 4
    "e06bf9a5-3a05-48ea-98eb-5b854bac333a", # Module 5
    "2a2ff7c4-b965-42b8-8bc4-458ff838513c", # Module 6
    "53291f90-a74a-4fb8-8e72-64c045eaaa55", # Module 7
]

if __name__ == "__main__":
    if not login():
        print("[-] Login failed.")
        exit(1)

    course_map = {}
    for i, ch_id in enumerate(chapter_ids):
        print(f"[*] Fetching menu for Module {i} using chapter ID {ch_id[:8]}...")
        url = f"{LMS_API}/direct-access/menu/{ch_id}"
        r = session.get(url, headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {JWT_TOKEN}",
        }, timeout=20)
        
        if r.status_code == 200:
            try:
                res = r.json()
                module_data = res.get("data", {})
                module_name = module_data.get("name", f"Module {i}")
                print(f"  [+] Fetched: {module_name}")
                course_map[f"module_{i}"] = module_data
            except Exception as e:
                print(f"  [-] Failed to parse JSON: {e}")
        else:
            print(f"  [-] Failed to fetch menu. Status code: {r.status_code}")

    with open("course_materials_map.json", "w", encoding="utf-8") as f:
        json.dump(course_map, f, indent=2, ensure_ascii=False)
    print("[+] Saved course materials map to course_materials_map.json")
