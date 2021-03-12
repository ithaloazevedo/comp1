def second_index(text: str, symbol: str) -> [int, None]:
    return text.find(symbol, text.find(symbol) + 1) if  text.count(symbol) >= 2 else None