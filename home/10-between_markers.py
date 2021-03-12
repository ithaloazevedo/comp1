def between_markers(text: str, begin: str, end: str) -> str:
    b = text.find(begin)
    e = text.find(end)
    if(b!=-1):
        b+=len(begin)
    else:
        b = 0
    if(e==-1):
        e = len(text)
    return text[b:e]

