#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""


import requests

def top_ten(subreddit):
    # Construct the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set the headers to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)
    
    # Check if the response status code is not 200 (OK)
    if response.status_code != 200:
        print("none")
        return
    
    try:
        # Attempt to parse the JSON response
        results = response.json().get("data")
        if results:
            # Loop through the first 10 posts and print their titles
            for post in results.get("children", [])[:10]:
                print(post.get("data").get("title"))
        else:
            print("No data found")
    except ValueError:
        # Handle the case where the response is not valid JSON
        print("Invalid JSON response")
