import requests

# Define the API endpoint
url = "https://api.socialverseapp.com/users/get_all?page=1&page_size=1000"

# Define the headers with API Key
headers = {
    "Content-Type": "application/json",
    "Flic-Token": "flic_11d3da28e403d182c36a3530453e290add87d0b4a40ee50f17611f180d47956f"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    print("Response Data:", response.json())  # Print JSON response
else:
    print(f"Error: {response.status_code}, Message: {response.text}")  # Print error details