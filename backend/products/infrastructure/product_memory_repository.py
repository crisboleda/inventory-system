from domain.product_repository import ProductRepository
from domain.product import Product


class ProductMemoryRepository(ProductRepository):

    products = []

    def get(self) -> list[Product]:
        return self.products

    def create(self, product: Product):
        self.products.append(product)
