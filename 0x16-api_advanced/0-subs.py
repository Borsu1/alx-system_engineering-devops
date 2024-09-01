#!/usr/bin/python3
""" Reddit Subscriber Count Module """
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        number_of_subscribers = data.get("subscribers")
        return subscribers
    else:
        return 0
