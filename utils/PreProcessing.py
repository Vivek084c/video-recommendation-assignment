import requests
import os
import logging
from box import Box


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

if __name__ == "__main__":
    pass