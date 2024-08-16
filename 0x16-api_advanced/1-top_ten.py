#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints titles of the first 10 hot posts or None if the
        subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(
        url, headers=headers, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


# Example usage
top_ten('python')
