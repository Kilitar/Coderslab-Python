import requests
import re

r = requests.get("https://lms.coderslab.cz/login")
print("Status:", r.status_code)
print("URL:", r.url)

# Find all input fields
inputs = re.findall(r"<input[^>]+>", r.text)
for inp in inputs:
    print("INPUT:", inp)

# Find meta csrf
metas = re.findall(r"<meta[^>]+>", r.text)
for m in metas:
    if "csrf" in m.lower() or "token" in m.lower():
        print("META:", m)

# Find any hidden fields
hidden = re.findall(r'type=["\']hidden["\'][^>]*>', r.text)
for h in hidden:
    print("HIDDEN:", h)

# Save full page
with open("login_inspect.html", "w", encoding="utf-8") as f:
    f.write(r.text)
print("\nUlozeno do login_inspect.html")
