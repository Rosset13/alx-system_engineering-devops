#!/usr/bin/python3
"""
This module defines the recurse function.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list of titles
    of all hot articles for a given subreddit.

    :param subreddit: The name of the subreddit to query.
    :param hot_list: List to store the titles of hot articles.
    :param after: The ID of the last item on the previous page.
    :return: List of titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after', None)

            if posts:
                hot_list.extend([post.get('data', {}).get('title', None) for post in posts])

            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
        else:
            return None
    except requests.RequestException:
        return None

