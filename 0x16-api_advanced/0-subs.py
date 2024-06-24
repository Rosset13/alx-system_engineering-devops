#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit JSON metadata
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Define custom User-Agent
    headers = {'User-Agent': 'Python:subscribers.counter:v1.0 (by /u/yourusername)'}
    
    try:
        # Make the request
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid, return 0
            return 0
    except requests.RequestException:
        # Handle any request exceptions
        return 0

