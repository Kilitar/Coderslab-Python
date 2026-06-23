import json

with open("lms_api_data.json", encoding="utf-8") as f:
    data = json.load(f)

for key, val in data.items():
    print(f"\n=== {key} ===")
    print(json.dumps(val, indent=2, ensure_ascii=False)[:2000])
