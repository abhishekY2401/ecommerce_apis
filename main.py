from fastapi import Body, FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.models import Product, Order, UpdatedProduct
from db import connect_to_database
from typing import Annotated, List
from schemas.productEntity import productEntity, productsEntity
from schemas.orderEntity import orderEntity, ordersEntity


app = FastAPI()

db = connect_to_database()
product_collection = "product"
order_collection = "order"


@app.get("/")
async def root():
    return {"message": "Hello World"}

# APIs to create
# create product


@app.post("/create_product", response_model=Product)
async def create_product(product: Annotated[Product, Body(embed=True)]):
    try:
        product = jsonable_encoder(product)
        new_product = db[product_collection].insert_one(product)
        created_product = db[product_collection].find_one(
            {"_id": new_product.inserted_id})
        if created_product:
            # print({"_id": str(created_product["_id"])})
            return productEntity(created_product)
    except Exception as e:
        return e


@app.get("/products", response_model=list[Product])
async def get_products(page: int = 1, limit: int = 10):
    try:
        return productsEntity(db[product_collection].find({}).skip((page-1)*limit).limit(limit))
    except Exception as e:
        return e


@app.get("/product/{product_id}", response_model=Product)
async def update_product(product_id: str, product: Annotated[UpdatedProduct, Body(embed=True)]):
    try:
        updated_item = jsonable_encoder(product)

    except Exception as e:
        return e


@app.post("/create_order", response_model=Order)
async def create_order(order: Annotated[Order, Body(embed=True)]):
    try:
        order = jsonable_encoder(order)
        new_order = db[order_collection].insert_one(order)
        print(new_order)
        created_order = db[order_collection].find_one(
            {"_id": new_order.inserted_id})
        if created_order:
            # print({"_id": str(created_product["_id"])})
            return orderEntity(created_order)
    except Exception as e:
        return e


@app.get("/orders", response_model=List[Order])
async def get_orders(page: int = 1, limit: int = 10):
    try:
        return ordersEntity(db[order_collection].find({}).skip((page-1)*limit).limit(limit))
    except Exception as e:
        return e
