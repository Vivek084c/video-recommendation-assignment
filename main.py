# import logging
# import os

# # Ensure the "logs" directory exists
# log_dir = 'logs'
# os.makedirs(log_dir, exist_ok=True)

# # logging configuration
# logger = logging.getLogger('Stage_1_Data_prerpcessing')
# logger.setLevel('DEBUG')

# # Clear any existing handlers
# logger.handlers = []

# console_handler = logging.StreamHandler()
# console_handler.setLevel('DEBUG')

# log_file_path = os.path.join(log_dir, 'Stage_1_Data_prerpcessing.log')
# file_handler = logging.FileHandler(log_file_path)
# file_handler.setLevel('DEBUG')

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)


# import os
# from dotenv import load_dotenv
# load_dotenv()
# from utils.PreProcessing import preprocessing



# app=FastAPI()
# app.include_router(users.APIRouter)


from fastapi import FastAPI
from routes import users  # Import users router

app = FastAPI()

# ✅ Include the users router
app.include_router(users.router)

# app = FastAPI()

# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to FastAPI!"}

# # Endpoint to return user info
# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id, "name": "John Doe"}

# # POST request to receive JSON data
# @app.post("/submit/")
# def submit_data(data: dict):
#     return {"message": "Data received", "data": data}




# custome end points
# username = "afrobeezy"
# @app.get("/getUserData/{username}")
# def get_user_data(username: str):
#     base_url_feed = os.getenv("BASE_URL_FEED_USER")
#     print(base_url_feed+username)
#     obj = preprocessing()
#     output = obj.get_user_feed(base_url_feed = base_url_feed, username = username)
#     output = output.posts[0]["topic"]
#     return output







