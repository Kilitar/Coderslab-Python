"""
Systematicky prohledava LMS pro materialy kurzu pres HTTP.
Zkusi GraphQL, REST, i prime URL patterny.
"""
import re
import json
import requests
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://lms.coderslab.cz"
LOGIN_CHECK_URL = f"{BASE_URL}/login_check"
COURSE_ID = "ONL_DTL_D_7979"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"
DOWNLOAD_DIR = Path("DATA") / "SESSION2_MATERIALS"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
})


def login():
    r = session.get(f"{BASE_URL}/login")
    payload = {"_username": EMAIL, "_password": PASSWORD, "_rememberMe": "on"}
    form = re.search(r"<form[^>]+action=[\"']([^\"']+)[\"']", r.text)
    post_url = urljoin(BASE_URL, form.group(1)) if form else LOGIN_CHECK_URL
    resp = session.post(post_url, data=payload, allow_redirects=True)
    ok = resp.url.rstrip("/") != f"{BASE_URL}/login".rstrip("/")
    print(f"[{'+'if ok else'-'}] Login -> {resp.url}")
    return ok


def get(path, **kwargs):
    url = urljoin(BASE_URL, path)
    try:
        r = session.get(url, timeout=15, **kwargs)
        if "login" in r.url and r.url != url:
            return None
        return r
    except Exception as e:
        print(f"  Error: {e}")
        return None


def post(path, **kwargs):
    url = urljoin(BASE_URL, path)
    try:
        r = session.post(url, timeout=15, **kwargs)
        return r
    except Exception as e:
        print(f"  Post Error: {e}")
        return None


def save_json(name, data):
    with open(name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    print(f"  -> Ulozeno: {name}")


if not login():
    exit(1)

# -----------------------------------------------
# 1. Try fetching main app JS to find API pattern
# -----------------------------------------------
print("\n[1] Hledam main JS soubor...")
r = get("/static/js/main.3949d687.chunk.js")
if r and r.status_code == 200:
    js = r.text
    print(f"    Delka main.js: {len(js)}")
    
    # Find URL-like strings
    paths = re.findall(r'"(/[a-zA-Z][a-zA-Z0-9/_\-]{3,50})"', js)
    paths = list(dict.fromkeys(paths))
    print(f"    URL cesty v main.js ({len(paths)}):")
    for p in paths:
        print(f"      {p}")
    
    # Look for fetch calls
    fetches = re.findall(r'fetch\(["\']([^"\']+)["\']', js)
    if fetches:
        print(f"    Fetch calls: {fetches}")
    
    # Look for axios/http calls
    axios = re.findall(r'\.get\(["\']([^"\']+)["\']', js)
    if axios:
        print(f"    .get calls: {axios[:10]}")
    
    # Save main.js for manual inspection
    with open("main_js.txt", "w", encoding="utf-8") as f:
        f.write(js)
    print("    -> Ulozeno main_js.txt")
else:
    print("    Nepodarilo se nacist main.js")

# -----------------------------------------------
# 2. Try GraphQL
# -----------------------------------------------
print("\n[2] Zkousim GraphQL endpointy...")
for gql_path in ["/graphql", "/api/graphql", "/v1/graphql", "/gql"]:
    r = get(gql_path)
    if r and r.status_code != 404:
        print(f"    {gql_path} -> {r.status_code} ({r.headers.get('Content-Type', '')})")

# Try GraphQL introspection
for gql_path in ["/graphql", "/api/graphql"]:
    r = post(gql_path, json={"query": "{ __schema { types { name } } }"})
    if r and r.status_code == 200:
        try:
            data = r.json()
            print(f"    GraphQL introspection OK na {gql_path}!")
            save_json("graphql_schema.json", data)
        except Exception:
            pass

# -----------------------------------------------
# 3. Inspect actual course page for JSON in script tags
# -----------------------------------------------
print("\n[3] Hledam embedded JSON v strance kurzu...")
session.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
r = get(f"/course/{COURSE_ID}")
if r and r.status_code == 200:
    html = r.text
    
    # Look for JSON in script tags
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.DOTALL)
    for i, sc in enumerate(scripts):
        if "{" in sc and len(sc) > 50:
            print(f"  Script #{i}: {sc[:200]}")
    
    # Look for data- attributes
    data_attrs = re.findall(r'data-[a-z-]+=["\']{([^"\']+)}["\']', html)
    if data_attrs:
        print(f"  Data attributes: {data_attrs[:5]}")

# -----------------------------------------------
# 4. Try known LMS patterns (Symfony/API Platform)
# -----------------------------------------------
print("\n[4] Zkousim Symfony/API Platform patterny...")
session.headers["Accept"] = "application/json"
session.headers["X-Requested-With"] = "XMLHttpRequest"

api_paths = [
    f"/api/courses/{COURSE_ID}",
    f"/api/courses/{COURSE_ID}/chapters",
    f"/api/courses/{COURSE_ID}/lessons",
    f"/api/courses/{COURSE_ID}/materials",
    f"/api/courses/{COURSE_ID}/attachments",
    "/api/me",
    "/api/profile",
    "/api/user",
]

for path in api_paths:
    r = get(path)
    if r and r.status_code == 200:
        ct = r.headers.get("Content-Type", "")
        if "json" in ct:
            try:
                data = r.json()
                print(f"  [+] {path} -> JSON: {str(data)[:200]}")
                save_json(f"api_{path.replace('/', '_')}.json", data)
            except Exception:
                print(f"  [+] {path} -> {r.status_code} (not JSON)")
        elif len(r.text) > 5000:
            print(f"  [+] {path} -> {r.status_code} HTML ({len(r.text)} chars)")
        else:
            print(f"  [ ] {path} -> {r.status_code}")
    else:
        status = r.status_code if r else "ERR"
        print(f"  [ ] {path} -> {status}")

print("\nHotovo. Zkontroluj api_*.json soubory a main_js.txt")
