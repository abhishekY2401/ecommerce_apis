def productEntity(item) -> dict:
    return {
        "id": item["id"],
        "name": item["name"],
        "price": item["price"],
        "available_quantity": item["available_quantity"],
        "createdAt": item["createdAt"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
