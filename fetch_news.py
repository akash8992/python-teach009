import requests

# Replace 'API_KEY' with your actual API key from NewsAPI
API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'

# Define the URL for the NewsAPI request
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

# Send a GET request to the NewsAPI
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    print("Successfully fetched the news!")
    # Optional: Print some news data
    data = response.json()
    for article in data['articles'][:5]:  # Print the first 5 articles
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}\n")
else:
    print(f"Failed to fetch news. Status code: {response.status_code}")
