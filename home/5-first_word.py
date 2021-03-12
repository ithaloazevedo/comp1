def first_word(text: str) -> str:
    return text.replace(".", " ").replace(",", " ").split()[0]