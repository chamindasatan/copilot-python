from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

def getData():
    class Product(BaseModel):
        id: int
        name: str
        price: float
        description: str
        image: str

    class Customer(BaseModel):
        id: int
        name: str
        email: str
        phone: str
        address: str

    class Order(BaseModel):
        id: int
        product_id: int
        customer_id: int
        quantity: int
        total: float

    products = [Product(id=i, name=f'Product {i}', price=10.0*i, description=f'Description {i}', image=f'Image {i}') for i in range(10)]
    customers = [Customer(id=i, name=f'Customer {i}', email=f'customer{i}@example.com', phone=f'123456789{i}', address=f'Address {i}') for i in range(10)]
    orders = [Order(id=i, product_id=i, customer_id=i, quantity=i, total=10.0*i) for i in range(10)]
    return Product,Customer,Order,products,customers,orders

Product, Customer, Order, products, customers, orders = getData()

@app.get("/products")
async def get_products():
    return products

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return products[product_id]

@app.post("/products")
async def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    products[product_id] = product
    return product

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return products.pop(product_id)

@app.get("/customers")
async def get_customers():
    return customers

@app.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    return customers[customer_id]

@app.post("/customers")
async def add_customer(customer: Customer):
    customers.append(customer)
    return customer

@app.put("/customers/{customer_id}")
async def update_customer(customer_id: int, customer: Customer):
    customers[customer_id] = customer
    return customer

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    return customers.pop(customer_id)

@app.get("/orders")
async def get_orders():
    return orders

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    return orders[order_id]

@app.post("/orders")
async def add_order(order: Order):
    orders.append(order)
    return order

@app.put("/orders/{order_id}")
async def update_order(order_id: int, order: Order):
    orders[order_id] = order
    return order

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    return orders.pop(order_id)