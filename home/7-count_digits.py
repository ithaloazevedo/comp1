def count_digits(text: str) -> int:
    """
        Counts the number of digits in a text
    """
    return sum(1 for c in text if c.isdigit())
