from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1
