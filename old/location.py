import requests
import json

# API URL
url = "http://api.open-notify.org/iss-now.json"

# Send a GET request to the API
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    latitude = data['iss_position']['latitude']  # Extract latitude
    longitude = data['iss_position']['longitude']  # Extract longitude
    print(f"Current ISS Location - Latitude: {latitude}, Longitude: {longitude}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
