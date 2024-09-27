#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers on a given Reddit subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']
        print("OK")
        return subscribers
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    print("OK")
    return 0
