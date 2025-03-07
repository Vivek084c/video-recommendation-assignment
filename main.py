# from fastapi import FastAPI
# from pydantic import BaseModel

# # Initialize FastAPI app
# app = FastAPI()

# # Sample in-memory database
# items = ["vivek"]

# # Pydantic Model for request body validation
# class Item(BaseModel):
#     name: str
#     price: float
#     quantity: int

# # Root endpoint
# @app.get("/")
# def home():
#     return {"message": "Welcome to FastAPI!"}

# # GET all items
# @app.get("/items")
# def get_items():
#     return {"items": items}

# # POST a new item
# @app.post("/items")
# def create_item(item: Item):
#     items.append(item.dict())  # Store item in list
#     return {"message": "Item added successfully!", "item": item}


