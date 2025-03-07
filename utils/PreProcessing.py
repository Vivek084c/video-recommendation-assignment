import requests
import os
import logging
from box import Box
import datetime

# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('PreProcessing')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'PreProcessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



class preprocessing:
    def get_response(self, api:str, data_endpoint:str):
        """
        Returns the Box object for the json response for the provided endpoint
        Args:
        api : api key for the end point
        data_endpoint: endpoint to fetch data from 

        Returns:
        json object of the retrived data
        """
        logger.log(logging.INFO, "Started json file retriver ")
        # Define the headers with API Key
        headers = {
            "Content-Type": "application/json",
            "Flic-Token": api
        }
        logger.log(logging.INFO, "Created the required header file")


        # Send GET request
        logger.log(logging.INFO, "Successfully Hit the endpoint")
        response = requests.get(data_endpoint, headers=headers)
        logger.log(logging.INFO, "Successfully got response from endpoint")

        # Check if request was successful
        if response.status_code == 200:
            logger.log(logging.INFO, "Response Successfull: ")
        else:
            logger.error(logging.ERROR,f"Error: {response.status_code}, Message: {response.text}")  # Print error details
        return Box(response.json())
    
    def get_user_feed(self, base_url_feed, username):
        """
        Returns the feed for a paticular user
        Args:
        base_url_feed : base url to hit the feet retrival endpoint
        username : username for which the feeed needs to be retrived
        Returns:
        Box object of the feed for the user
        """
        final_url = base_url_feed + username
        response = requests.get(final_url)
        return Box(response.json())
    
    

    def extract_features(self, post):
        """
        Extract key features from post data, grouped by category.
        Args : 
        post - input post box object
        return - dict with feature map
        """
        
        #Engagement Features
        engagement_features = {
            "view_count": post.view_count,
            "upvote_count": post.upvote_count,
            "comment_count": post.comment_count,
            "exit_count": post.exit_count,
            "rating_count": post.rating_count,
            "average_rating": post.average_rating,
            "share_count": post.share_count,
            "bookmark_count": post.bookmark_count,
        }

        #Content Features
        content_features = {
            "category": post.category.name,
            "topic": post.topic.name,
            "title": post.title,
            "tags": post.tags,
        }

        #Other Features (User Behavior & Time-Based)
        timestamp = post.created_at / 1000  # Convert from milliseconds
        post_date = datetime.datetime.utcfromtimestamp(timestamp)  # Correct usage of datetime
        post_age_days = (datetime.datetime.utcnow() - post_date).days  # Compute post age in days

        other_features = {
            "username": post.username,
            "user_type": post.user_type,
            "upvoted": post.upvoted,
            "bookmarked": post.bookmarked,
            "following": post.following,
            "post_age_days": post_age_days,  # Age of post in days
        }

        # Return as structured dictionary
        return {
            "engagement_features": engagement_features,
            "content_features": content_features,
            "other_features": other_features
        }
        

if __name__ == "__main__":
    pass