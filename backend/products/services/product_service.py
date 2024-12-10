from domain.product import Product
from domain.product_repository import ProductRepository


class ProductService:

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_products(self) -> list[Product]:
        return self.product_repository.get()
