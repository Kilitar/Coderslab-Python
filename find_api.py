"""
Hleda URL patterny v bundlovanem JS souboru LMS.
"""
import re
import requests

BASE_URL = "https://lms.coderslab.cz"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

js_url = f"{BASE_URL}/static/js/2.b89434f0.chunk.js"
print(f"[*] Stahuji JS: {js_url}")
r = session.get(js_url, timeout=30)
js = r.text
print(f"[*] Delka: {len(js)}")

# Broad search - anything that looks like a URL path with letters
paths = re.findall(r'"(/[a-zA-Z][a-zA-Z0-9_\-/]{4,60})"', js)
unique = list(dict.fromkeys(paths))
print(f"\nNalezeno {len(unique)} URL cest, prvnich 50:")
for p in unique[:50]:
    print(f"  {p}")

print("\n--- Hledame 'course', 'material', 'download' ---")
for kw in ["course", "material", "download", "attachment", "lesson", "file"]:
    hits = [p for p in unique if kw in p.lower()]
    if hits:
        print(f"\n[{kw}]:")
        for h in hits[:10]:
            print(f"  {h}")

# Hledame templatey (napr. /api/v1/courses/{id}/materials)
templates = re.findall(r'"(/[^"]*\{[^"]*\}[^"]*)"', js)
if templates:
    print("\nURL templaty:")
    for t in templates[:20]:
        print(f"  {t}")
