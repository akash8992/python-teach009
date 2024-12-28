import requests

# API endpoint and key
API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "3805f6bbabcb42b3a0c08a489baf603d"

# Parameters for the API request
params = {
    "country": "us",
    "apiKey": API_KEY
}

# Making the API request
response = requests.get(API_URL, params=params)

# Checking if the request was successful
if response.status_code == 200:
    # Printing the JSON response
    print(response.json())
else:
    print(f"Error: {response.status_code}")