NUTRIENT_MAP = {
    "vitamin c": "vitamin_c",
    "ascorbic acid": "vitamin_c",
    "protein": "protein",
    "calcium": "calcium",
    "iron": "iron",
    "thiamine": "vitamin_b1",
    "thiamine mononitrate": "vitamin_b1",
    "pyridoxine hcl": "vitamin_b6",
}

UNIT_MAP = {
    "mg": "mg",
    "milligrams": "mg",
    "g": "g",
    "grams": "g",
    "mcg": "µg",
    "µg": "µg",
    "iu": "IU",
}


def normalize_nutrient(name):
    key = name.lower().strip()
    return NUTRIENT_MAP.get(key, key)


def normalize_unit(unit):
    if not unit:
        return None
    return UNIT_MAP.get(unit.lower(), unit)