from pathlib import Path
import json
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"

data = {
    "version": "1.0.0",
    "lastUpdated": datetime.utcnow().isoformat() + "Z",
    "totalPrompts": 0,
    "categories": [],
    "prompts": []
}

categories = set()

for meta in PROMPTS.rglob("metadata.yml"):
    category = meta.parent.parent.name
    categories.add(category)

    data["prompts"].append({
        "name": meta.parent.name,
        "path": str(meta.parent.relative_to(ROOT))
    })

data["categories"] = sorted(categories)
data["totalPrompts"] = len(data["prompts"])

with open(PROMPTS / "index.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Indexed {data['totalPrompts']} prompts.")
