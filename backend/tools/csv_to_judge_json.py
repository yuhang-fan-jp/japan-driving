import csv
import json

INPUT_CSV = "questions.csv"
OUTPUT_JSON = "questions.json"

result = []

with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        item = {
            "content": row["content"].strip(),
            "answer": row["answer"].strip().lower() in ("true", "1", "yes", "y")
        }

        # Cloudflare 图片 URL（可选）
        image_url = row.get("image_url", "").strip()
        if image_url:
            item["image_url"] = image_url

        result.append(item)

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"已生成 {OUTPUT_JSON}，共 {len(result)} 道题")