"""
Hleda v chunk JS souborech presny axios base URL a API volani.
"""
import re
import requests

BASE_URL = "https://lms.coderslab.cz"
session = requests.Session()

chunks = {
    5: "8abd68ad",
    8: "74ad860e",
    3: "58d7ba02",
    4: "cffd1888",
    9: "3104ab32",
}

for chunk_id, chunk_hash in chunks.items():
    url = f"{BASE_URL}/static/js/{chunk_id}.{chunk_hash}.chunk.js"
    r = session.get(url, timeout=30)
    js = r.text
    print(f"\n{'='*60}")
    print(f"CHUNK {chunk_id} ({len(js)} chars): {url}")
    print('='*60)

    # Look for baseURL
    base_urls = re.findall(r'baseURL["\s]*[:=]["\s]*["\'`]([^"\'`]+)["\'`]', js)
    if base_urls:
        print(f"baseURLs: {base_urls}")

    # Look for axios configuration
    axios_configs = re.findall(r'axios\.create\(\{([^}]{0,300})\}', js)
    for ac in axios_configs:
        print(f"axios.create: {ac}")

    # Look for any URL-like patterns that could be API base
    api_bases = re.findall(r'"(https?://[^"]{5,80})"', js)
    for ab in api_bases:
        if "lms" in ab.lower() or "api" in ab.lower() or "coderslab" in ab.lower():
            print(f"API URL: {ab}")

    # Look for template literals with variables (these are the actual API calls)
    # Pattern: `.get(`...${varname}...`)`
    template_gets = re.findall(r'\.(?:get|post|put|delete)\(([^)]{0,300})\)', js)
    for tg in template_gets:
        if "${" in tg or "material" in tg.lower() or "chapter" in tg.lower() or "attachment" in tg.lower():
            print(f"API call: {tg[:200]}")

    # Look for all string context around "attachment"
    for m in re.finditer(r"attach", js, re.IGNORECASE):
        ctx = js[max(0, m.start()-200):m.end()+200]
        if any(k in ctx for k in ["get(", "post(", "url", "fetch", "api", "lms"]):
            print(f"\nAttachment context:\n{ctx}\n")

    # Find where 'lms-api' is defined or referenced
    for m in re.finditer(r"lms-api", js, re.IGNORECASE):
        ctx = js[max(0, m.start()-100):m.end()+100]
        print(f"lms-api context: {ctx}")

    # Save the chunk for manual inspection if it's small enough
    if len(js) < 200000:
        with open(f"chunk_{chunk_id}.js", "w", encoding="utf-8") as f:
            f.write(js)
        print(f"-> Saved to chunk_{chunk_id}.js")
