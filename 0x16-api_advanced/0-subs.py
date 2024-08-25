#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 404:
            return 0
        results = response.json().get('data')
        return results.get('subscribers')
