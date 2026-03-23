import re

NUTRIENT_PATTERN = r"([A-Za-z\s]+?)\s+(\d+\.?\d*)\s*(mg|g|mcg|µg|IU)?"


def extract_nutrients(text):
    matches = re.findall(NUTRIENT_PATTERN, text, re.IGNORECASE)

    cleaned = []
    for name, amount, unit in matches:
        name = name.strip()
        if len(name) < 2:
            continue
        cleaned.append((name, amount, unit))

    return cleaned