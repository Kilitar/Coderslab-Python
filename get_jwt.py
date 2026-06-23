"""
Ziskava JWT token z LMS a pouziva ho pro download materialu.
"""
import re
import json
import requests
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://lms.coderslab.cz"
COURSE_ID = "ONL_DTL_D_7979"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"
DOWNLOAD_DIR = Path("DATA") / "SESSION2_MATERIALS"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
})

JWT_TOKEN = None


def login():
    global JWT_TOKEN
    r = session.get(f"{BASE_URL}/login")
    form = re.search(r"<form[^>]+action=[\"']([^\"']+)[\"']", r.text)
    post_url = urljoin(BASE_URL, form.group(1)) if form else f"{BASE_URL}/login_check"
    resp = session.post(post_url, data={
        "_username": EMAIL, "_password": PASSWORD, "_rememberMe": "on"
    }, allow_redirects=True)
    
    ok = resp.url.rstrip("/") != f"{BASE_URL}/login".rstrip("/")
    print(f"[{'+'if ok else'-'}] Login -> {resp.url}")
    return ok


def get_jwt():
    """Get JWT token from the LMS - might be in a cookie or from /api/jwt endpoint."""
    global JWT_TOKEN
    
    # Check cookies for JWT-like tokens
    for cookie in session.cookies:
        print(f"  Cookie: {cookie.name} = {cookie.value[:50]}...")
    
    # Try various JWT endpoints
    for path in ["/api/jwt", "/api/token", "/api/auth/token", "/jwt"]:
        r = session.get(urljoin(BASE_URL, path), timeout=10)
        ct = r.headers.get("Content-Type", "")
        if "json" in ct and r.status_code == 200:
            try:
                data = r.json()
                print(f"  JWT endpoint {path}: {str(data)[:200]}")
                if "token" in data:
                    JWT_TOKEN = data["token"]
                    return JWT_TOKEN
            except Exception:
                pass
    
    # Look for JWT in main page or a refresh
    r = session.get(f"{BASE_URL}/")
    # JWT tokens look like: xxxxx.yyyyy.zzzzz
    jwt_matches = re.findall(r'"jwt"\s*:\s*"([A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)"', r.text)
    if jwt_matches:
        JWT_TOKEN = jwt_matches[0]
        print(f"  JWT z home page: {JWT_TOKEN[:50]}...")
        return JWT_TOKEN
    
    return None


def api_get(path, headers=None):
    url = urljoin(BASE_URL, path)
    h = {}
    if JWT_TOKEN:
        h["Authorization"] = f"Bearer {JWT_TOKEN}"
    if headers:
        h.update(headers)
    
    for accept in ["application/json", "*/*"]:
        r = session.get(url, headers={**h, "Accept": accept}, timeout=15)
        if r.status_code == 200:
            ct = r.headers.get("Content-Type", "")
            if "json" in ct:
                try:
                    return r.json()
                except Exception:
                    pass
        elif r.status_code not in [404, 403]:
            print(f"  {path} -> {r.status_code}")
    return None


def sanitize(name):
    return re.sub(r'[\\/*?:"<>|]', "_", str(name)).strip(". ")[:120]


def download_file(url, filename=None):
    h = {}
    if JWT_TOKEN:
        h["Authorization"] = f"Bearer {JWT_TOKEN}"
    try:
        r = session.get(url, headers=h, stream=True, timeout=60)
        r.raise_for_status()
        if not filename:
            cd = r.headers.get("Content-Disposition", "")
            m = re.search(r'filename[^;=\n]*=(["\']?)([^"\';\n]+)\1', cd)
            filename = m.group(2).strip() if m else sanitize(url.split("/")[-1].split("?")[0])
        dest = DOWNLOAD_DIR / sanitize(filename)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        size = dest.stat().st_size
        print(f"  [+] {dest.name} ({size//1024} KB)")
        return True
    except Exception as e:
        print(f"  [-] {url}: {e}")
        return False


def explore_main_js():
    """Extract more patterns from main.js."""
    r = session.get(f"{BASE_URL}/static/js/main.3949d687.chunk.js")
    js = r.text
    
    # Find all string patterns around 'course', 'material', 'download', 'users'
    results = {}
    for kw in ["users/me", "jwt", "download", "material", "course", "attachment"]:
        # Get context around each keyword occurrence
        contexts = []
        for m in re.finditer(re.escape(kw), js, re.IGNORECASE):
            start = max(0, m.start() - 100)
            end = min(len(js), m.end() + 100)
            ctx = js[start:end]
            contexts.append(ctx)
        results[kw] = contexts[:5]
    
    with open("main_js_analysis.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("  -> main_js_analysis.json")
    
    # Specifically look for the users/me endpoint context
    print("\n  Context kolem 'users/me':")
    for m in re.finditer(r"users/me", js):
        start = max(0, m.start() - 200)
        end = min(len(js), m.end() + 200)
        print(f"  ...{js[start:end]}...")
        print()
    
    # Look for the base API URL
    print("\n  Hledam base API URL:")
    api_bases = re.findall(r'"(https?://[^"]+/api[^"]{0,30})"', js)
    for ab in api_bases[:5]:
        print(f"  {ab}")
    
    # Look for lms.coderslab in JS
    lms_urls = re.findall(r'"(https://lms\.coderslab[^"]+)"', js)
    for u in lms_urls[:10]:
        print(f"  LMS URL: {u}")
    
    return js


if not login():
    exit(1)

print("\n[*] Hledam JWT token...")
jwt = get_jwt()
print(f"[*] JWT: {jwt[:50] if jwt else 'nenalezen'}")

print("\n[*] Analyzuji main.js...")
js = explore_main_js()

# Try users/me with session cookies
print("\n[*] Volam users/me...")
for path in ["users/me", "/users/me", "/api/users/me", "/v1/users/me"]:
    r = session.get(urljoin(BASE_URL, path), timeout=10)
    ct = r.headers.get("Content-Type", "")
    print(f"  {path} -> {r.status_code} ({ct[:40]})")
    if "json" in ct and r.status_code == 200:
        data = r.json()
        print(f"  DATA: {str(data)[:300]}")
        with open("me.json", "w") as f:
            json.dump(data, f, indent=2)
