import re
import json
import requests
from urllib.parse import urljoin
import traceback

BASE_URL = "https://lms.coderslab.cz"
LMS_API = f"{BASE_URL}/lms-api"
EMAIL = "xeen@seznam.cz"
PASSWORD = "yE9m2MMh.C5qcBR"
INSTANCE_ID = "328"

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})
JWT_TOKEN = None

try:
    r = session.get(f"{BASE_URL}/login")
    form = re.search(r'<form[^>]+action=["\']([^"\']+)["\']', r.text)
    post_url = urljoin(BASE_URL, form.group(1)) if form else f"{BASE_URL}/login_check"
    session.post(post_url, data={"_username": EMAIL, "_password": PASSWORD, "_rememberMe": "on"}, allow_redirects=True)
    for c in session.cookies:
        if c.name == "jwt":
            JWT_TOKEN = c.value
    print(f"[+] JWT: {'OK' if JWT_TOKEN else 'chybi'}")

    with open("course_structure.json", encoding="utf-8") as f:
        cs = json.load(f)

    # Find chapter 0-6
    chapter_06 = None
    for module in cs["data"]["modules"]:
        for ch in module["chapters"]:
            if ch["slug"] == "0-6":
                chapter_06 = ch
                break

    cid = chapter_06["id"]
    print(f"Chapter 0-6 id: {cid}")

    def get(path, accept="application/json"):
        url = f"{LMS_API}/{path.lstrip('/')}"
        r = session.get(url, headers={
            "Accept": accept,
            "Authorization": f"Bearer {JWT_TOKEN}",
        }, timeout=15)
        ct = r.headers.get("Content-Type", "")
        return r, ct

    # Test endpoints
    paths = [
        f"chapter/{cid}",
        f"chapter/{cid}/materials",
        f"chapters/{cid}",
        f"chapters/{cid}/materials",
        f"course-instance/{INSTANCE_ID}/chapter/{cid}",
        f"course-instance/{INSTANCE_ID}/chapter/{cid}/materials",
        f"course-instance/{INSTANCE_ID}/chapters/0-6/materials",
        f"material/{INSTANCE_ID}/0-6",
    ]

    for path in paths:
        r, ct = get(path)
        print(f"  {path} -> {r.status_code} ({ct[:30]}): {r.text[:100]}")

    # Read and review endpoints
    print("\n/read and /review:")
    for path in ["material/328/0-6/read", "material/328/0-6/review"]:
        r, ct = get(path)
        print(f"  {path} -> {r.status_code}: {r.text[:100]}")

except Exception:
    traceback.print_exc()
