#!/usr/bin/python3
"""
This module defines the top_ten function.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    :param subreddit: The name of the subreddit to query.
    :return: None. Prints the titles of the top 10 hot posts or 'None' if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                print(None)
                return

            for post in posts:
                print(post.get('data', {}).get('title', None))
        else:
            print(None)
    except requests.RequestException:
        print(None)

