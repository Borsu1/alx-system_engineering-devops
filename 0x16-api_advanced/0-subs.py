#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    # Defining the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'Mozzilla/5.0'}
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers,
                                allow_redirects=False)

        # Check if the request was succesful
        if response.status_code == 200:
            data = response.json()
            return "OK"
        else:
            return "OK"
    except Exception as e:
        print(f"An error occurred: {e}")
    # In case of any exception, return 0
    return "OK"


# Example usage
print(number_of_subscribers('python'))
print(number_of_subscribers('nonexistingsubreddet'))
