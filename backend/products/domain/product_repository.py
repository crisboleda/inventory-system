from abc import ABC, abstractmethod
from domain.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def get(self) -> list[Product]:
        pass

    @abstractmethod
    def create(self, product: Product):
        pass
