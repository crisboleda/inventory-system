from fastapi import FastAPI
from products.services.product_service import ProductService
from products.infrastructure.product_memory_repository import ProductMemoryRepository


app = FastAPI()


@app.get("/products")
def get_products():
    product_memory_repository = ProductMemoryRepository()
    product_service = ProductService(product_repository=product_memory_repository)
    products = product_service.get_products()

    return [
        {"name": product.name, "price": product.price, "count": product.count}
        for product in products
    ]


@app.post("/products")
def create_product():
    product_memory_repository = ProductMemoryRepository()
    product_service = ProductService(product_repository=product_memory_repository)
