from fastapi import FastAPI
from fastapi import Response,HTTPException,status,Depends,APIRouter
import os
from dotenv import load_dotenv
from ..utils.PreProcessing import preprocessing
load_dotenv()

router=APIRouter(
    prefix="/user",tags=["user"]
)


#endpoint to get the usr data
@router.get("/getUserData/{username}")
def get_user_data(username: str):
    base_url_feed = os.getenv("BASE_URL_FEED_USER")
    print(base_url_feed+username)
    obj = preprocessing()
    output = obj.get_user_feed(base_url_feed = base_url_feed, username = username)
    output = output.posts[0]["topic"]
    return output