def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    text=','.join(phrases)
    return text.replace("right","left")
