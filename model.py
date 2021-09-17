from pydantic import BaseModel


class Product(BaseModel):
    product_id: int
    title: str


class Item(BaseModel):
    id: int
    title: str
    product_id: int
