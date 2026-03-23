import easyocr

reader = easyocr.Reader(['en'], gpu=False)


def extract_text(image_path):
    results = reader.readtext(image_path)
    texts = [text for (_, text, _) in results]
    return " ".join(texts)