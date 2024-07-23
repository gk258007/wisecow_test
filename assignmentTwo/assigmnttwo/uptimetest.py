import requests
import logging
from datetime import datetime

# Configuration: Define the URL to check and the expected status code
URL = "http://135.237.11.119:4499"
EXPECTED_STATUS_CODE = 200
LOG_FILE = "app_uptime.log"

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def check_application_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        
        if status_code == EXPECTED_STATUS_CODE:
            message = f"Application is UP. Status Code: {status_code}"
            logging.info(message)
            print(message)
        else:
            message = f"Application is DOWN. Status Code: {status_code}. Expected: {EXPECTED_STATUS_CODE}"
            logging.error(message)
            print(message)
    
    except requests.RequestException as e:
        message = f"Application is DOWN. Error: {e}"
        logging.error(message)
        print(message)

if __name__ == "__main__":
    check_application_status(URL)
