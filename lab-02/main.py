# Lab-02
# To run the application: uvicorn main:app --reload --port 8081
# Swagger UI: http://127.0.0.1:8081/docs

from fastapi import FastAPI, HTTPException

## Define `app` instance
app = FastAPI(
    title="Product Catalog Service",
    description="A simple FastAPI application for managing Product Catalog.",
    version="1.0.0"
)


## Prepare data
products = [
    {"product_id": 1, "name": "Laptop (For Office)", "category": "electronics", "price": 1200.0, "in_stock": True},
    {"product_id": 2, "name": "Wireless Mouse", "category": "electronics", "price": 25.5, "in_stock": True},
    {"product_id": 3, "name": "Office Chair", "category": "furniture", "price": 180.0, "in_stock": False},
    {"product_id": 4, "name": "Desk Lamp", "category": "furniture", "price": 35.0, "in_stock": True},
    {"product_id": 5, "name": "Python Programming", "category": "books", "price": 45.0, "in_stock": True}
]


## Exercise 1
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["product_id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


## Exercise 2 & Exercise 3 (optional `keyword` query parameter)
@app.get("/products/")
def get_products(category: str | None = None,
                 min_price: float | None = None,
                 max_price: float | None = None,
                 in_stock: bool | None = None,
                 keyword: str | None = None):
    result = products

    # Explain: For each `product`` in `result`, include that `product` in the new `list` only if its category matches.
    if category is not None:
        result = [
            product for product in result
            if product["category"] == category
        ]

    if min_price is not None:
        result = [
            product for product in result
            if product["price"] >= min_price
        ]

    if max_price is not None:
        result = [
            product for product in result
            if product["price"] <= max_price
        ]

    if in_stock is not None:
        result = [
            product for product in result
            if product["in_stock"] == in_stock
        ]

    ## Exercise 3 (optional `keyword` query parameter)
    if keyword is not None:
        result = [
            product for product in result
            if keyword.lower() in product["name"].lower()
        ]

    return result


## Exercise 4
@app.get("/")
def root():
    return {"service": "Product Catalog Service", "course": "504070"}


@app.get("/health")
def health():
    return {"status": "healthy"}
