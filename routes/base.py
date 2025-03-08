from fastapi import FastAPI
from fastapi import Response,HTTPException,status,Depends,APIRouter
import os
import requests
from box import Box
from utils.PreProcessing import preprocessing
from dotenv import load_dotenv
load_dotenv()


router = APIRouter(
    prefix="/base", tags=["posts"]
)

#test endpoint to get all the posts
@router.get("/getallposts")
def get_all_posts_views():
    base_url = os.getenv("POST_BASE_URL")
    output = Box(requests.get(base_url).json())
    return output.posts[0]

#test endpoitn to get all the user data
@router.get("/getalluserdata")
def get_all_posts_views():
    base_url = os.getenv("USER_BASE_URL")
    api = os.getenv("Flic-Token")
    headers = {
        "Content-Type": "application/json",
        "Flic-Token": api
    }
    output = Box(requests.get(base_url, headers=headers).json())
    return output.users[0]
    

#endpoint to get the uesr data
@router.get("/getUserData/{username}")
def get_user_data(username: str):
    print("hit --------")
    base_url_feed = os.getenv("BASE_URL_FEED_USER")
    print(base_url_feed+username)
    obj = preprocessing()
    output = obj.get_user_feed(base_url_feed = base_url_feed, username = username)
    return output.posts