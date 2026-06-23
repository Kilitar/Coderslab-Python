import re

with open("course_page.html", encoding="utf-8") as f:
    html = f.read()

print("Delka HTML:", len(html))

title = re.findall(r"<title>([^<]+)</title>", html)
print("Title:", title)

hrefs = re.findall(r'href="([^"]+)"', html)
print("\nHrefs:")
for h in hrefs[:30]:
    print(" ", h)

scripts = re.findall(r"<script[^>]*src=['\"]([^'\"]+)['\"]", html)
print("\nScripts:")
for s in scripts[:10]:
    print(" ", s)

# Look for API or route patterns
api_routes = re.findall(r"['\"]/(api|course|material|lesson)[^'\"]{0,80}['\"]", html)
print("\nAPI/route patterns:")
for a in api_routes[:20]:
    print(" ", a)

# Look for any JSON-like data embedded in page
json_data = re.findall(r"window\.__[A-Z_]+\s*=\s*(\{[^;]{0,300})", html)
print("\nWindow vars:")
for d in json_data[:3]:
    print(" ", d[:200])
