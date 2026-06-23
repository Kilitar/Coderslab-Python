"""
Hleda endpoint pro seznam materialu v kapitole.
Zkusi vsechny rozumne variace.
"""
import re
import json
import requests
from urllib.parse import urljoin

BASE_URL = "https://lms.coderslab.cz"
LMS_API = f"{BASE_URL}/lms-api"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"
INSTANCE_ID = "328"

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})
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
    print(f"[+] JWT: {'OK' if JWT_TOKEN else 'CHYBI'}")


def try_get(path):
    url = f"{LMS_API}/{path.lstrip('/')}"
    r = session.get(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {JWT_TOKEN}",
    }, timeout=15)
    ct = r.headers.get("Content-Type", "")
    body = r.text
    is_json = "json" in ct or body.strip().startswith(("{", "["))
    if is_json and r.status_code == 200:
        try:
            data = json.loads(body)
            return r.status_code, data
        except Exception:
            pass
    return r.status_code, body[:80] if not is_json else body[:80]


login()

# We know 0-6 -> dd28a343 and 1-4 -> 4f7cd228
# Let's use known materialId to get chapter info and find the endpoint
# Start from dd28a343 (chapter 0-6) and look at its data structure
test_slug = "0-6"
test_mat_id = "dd28a343-5fdb-4525-8030-d680ca0ae9e8"

print(f"\n[*] Inspecting known material {test_mat_id[:8]} in chapter {test_slug}:")
status, data = try_get(f"material/{INSTANCE_ID}/{test_slug}/{test_mat_id}")
if isinstance(data, dict):
    print(json.dumps(data, indent=2, ensure_ascii=False)[:2000])

# Try to get course-instance endpoint
print(f"\n[*] Trying course-instance endpoints:")
for path in [
    f"course-instance/{INSTANCE_ID}",
    f"course-instances/{INSTANCE_ID}",
    f"instance/{INSTANCE_ID}",
    f"instances/{INSTANCE_ID}",
    f"course-instance/{INSTANCE_ID}/chapters",
    f"course-instance/{INSTANCE_ID}/materials",
]:
    status, result = try_get(path)
    if isinstance(result, dict):
        print(f"  [+] {path}: {str(result)[:200]}")
    else:
        print(f"  [ ] {path} -> {status}")

# Try chapter list endpoint variations
print(f"\n[*] Trying chapter material list endpoints for slug 0-4:")
for path in [
    f"chapter/0-4/materials",
    f"chapter/0-4",
    f"chapters/0-4/materials",
    f"material/{INSTANCE_ID}/0-4/materials",
    f"material/{INSTANCE_ID}/0-4/list",
    f"course-instance/{INSTANCE_ID}/material/0-4",
    f"course-instance/{INSTANCE_ID}/materials/0-4",
    f"course-instance/{INSTANCE_ID}/chapter/0-4",
    f"access/instance/{INSTANCE_ID}/chapter/0-4",
    f"access/instance/{INSTANCE_ID}",
]:
    status, result = try_get(path)
    if isinstance(result, dict):
        print(f"  [+] {path}: {str(result)[:300]}")
    elif status == 403:
        body = result if isinstance(result, str) else str(result)
        print(f"  [403] {path}: {body[:80]}")
    else:
        print(f"  [ ] {path} -> {status}")
