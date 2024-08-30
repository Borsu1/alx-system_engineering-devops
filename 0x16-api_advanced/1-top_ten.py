#!/usr/bin/python3
import requests
import sys


def top_ten(subreddit):
    """
    Queries Reddit API and prints the titles of the first 10 hot posts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data").get("children")
    top_ten_posts = "\n".join(post.get("data").get("title") for post in data)
    print(top_ten_posts)
