#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot
        posts listed for a given subreddit.
    """
import requests


def top_ten(subreddit):
    # Define the URL for the subreddit's hot.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(
                url, headers=headers, allow_redirects=False
                )
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid, print None
            print(None)
    except requests.RequestException:
        # Handle any request exceptions
        print(None)
