#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    # Prints the titles of the top 10 hot posts for a given subreddit.
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    headers = {'User-agent': 'your bot 0.1'}
    response = requests.get(url, headers=headers)
    print(response.text)  # Print the raw response for debugging
    if response.status_code == 200:
        try:
            results = response.json().get("data")
            if results:
                for post in results.get("children", []):
                    print(post.get("data").get("title"))
            else:
                print("No data found")
        except ValueError:
            print("Invalid JSON response")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-main.py <subreddit>")
    else:
        top_ten(sys.argv[1])
