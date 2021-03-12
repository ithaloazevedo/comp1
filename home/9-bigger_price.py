
def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda i:i["price"], reverse=True)[:limit:1]
