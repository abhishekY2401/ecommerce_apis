from models.PyObjectId import PydanticObjectId
from pydantic import BaseModel, Field as PydanticField
from bson import ObjectId
from datetime import datetime
from typing import List


# create a product model

class Product(BaseModel):
    id: int
    name: str
    price: float
    available_quantity: int
    createdAt: datetime


# create Updated Product Model


class UpdatedProduct(BaseModel):
    name: str | None
    price: float | None
    available_quantity: int | None
    createdAt: datetime | None


# Order Model


class Order(BaseModel):
    id: int
    items: List[dict[str, int]]
    total_amount: int
    user_address: dict[str, str]
    createdAt: datetime
    updatedAt: datetime
