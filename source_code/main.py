import os
import pandas as pd
from ocr import extract_text
from parser import extract_nutrients
from normalizer import normalize_nutrient, normalize_unit

INPUT_DIR = "sample_images"
OUTPUT_FILE = "output/nutrition_data.csv"


def process_image(image_path):
    text = extract_text(image_path)
    nutrients = extract_nutrients(text)

    rows = []
    for name, amount, unit in nutrients:
        rows.append({
            "product_image": os.path.basename(image_path),
            "nutrient_name_raw": name,
            "nutrient_name_standard": normalize_nutrient(name),
            "amount": float(amount),
            "unit": normalize_unit(unit)
        })

    return rows


def main():
    all_rows = []

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(INPUT_DIR, file)
            rows = process_image(path)
            all_rows.extend(rows)

    df = pd.DataFrame(all_rows)
    os.makedirs("output", exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved output to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()