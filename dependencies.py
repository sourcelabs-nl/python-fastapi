from model import Product


class ProductService:
    products = None

    def __init__(self):
        self.products = [Product(product_id=1, title='product')]

    def find_product(self, product_id) -> Product:
        for p in self.products:
            if p.product_id == product_id:
                return p
