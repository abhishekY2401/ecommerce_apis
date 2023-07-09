def orderEntity(order) -> dict:
    return {
        "id": order["id"],
        "items": order["items"],
        "total_amount": order["total_amount"],
        "user_address": order["user_address"],
        "createdAt": order["createdAt"],
        "updatedAt": order["updatedAt"],
    }


def ordersEntity(entity) -> list:
    return [orderEntity(order) for order in entity]
