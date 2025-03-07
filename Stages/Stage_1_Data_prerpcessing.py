import sys
import os
# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv
from utils.PreProcessing import preprocessing
load_dotenv()
import logging

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

# ----------------------------------------
class main:
    def fetch_data(self):
        logger.log(logging.INFO, "Completed >>>> Fetching the API key and endpoint for data Fetching")
        api = os.getenv("Flic-Token")
        # base_url = os.getenv("API_BASE_URL")
        data_url = os.getenv("DATA_FETCH_URL")
        logger.log(logging.INFO, "Started >>>> Fetching the API key and endpoint for data Fetching ")

        logger.log(logging.INFO, "Started >>>> Getting the response from https request")
        obj = preprocessing()
        json_out = obj.get_response(api = api, data_endpoint=data_url)
        logger.log(logging.INFO, "Completed >>>> Getting the response from https request")

        return json_out
    
if __name__ == "__main__":
    pass

