
def popular_words(text: str, words: list) -> dict:
    TEXT = text.lower().split()
    result = {}
    for word in words:
        result[word] = TEXT.count(word)
    return result
