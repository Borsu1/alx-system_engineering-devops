#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to get the titles
        of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        Default is an empty list.
        after (str): The 'after' parameter for pagination.
        Default is None.

    Returns:
        list: A list containing the titles of all hot articles
        for the given subreddit.
        None: If the subreddit is invalid or no results are found.

    Example:
        >>> recurse('python')
        ['Title 1', 'Title 2', 'Title 3', ...]
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        return None if not hot_list else hot_list

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

# Example usage:
# print(recurse('python'))
