
def is_text_empty(text):
        res = text is None or not text.strip()
        if res:
            print("📛 CANCELED 📛")
        return res