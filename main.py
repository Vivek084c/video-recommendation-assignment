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
# dsafads


from Stages.Stage_1_Data_prerpcessing import main
import logging
import os

# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('Stage_1_Data_prerpcessing')
logger.setLevel('DEBUG')

# Clear any existing handlers
logger.handlers = []

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'Stage_1_Data_prerpcessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def Main():
    logger.log(logging.INFO, "Started >>>> started preprocessing")
    obj = main()
    outfile = obj.fetch_data()
    logger.log(logging.INFO, "Completed >>>> started preprocessing")


if __name__ == "__main__":
    Main()