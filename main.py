from fastapi import FastAPI, Depends

from model import Product
from dependencies import ProductService

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products/{product_id}", response_model=Product)
def read_item(product_id: int, service: ProductService = Depends(ProductService)):
    return service.find_product(product_id)