#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to get the titles
    of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}" if after else "?limit=100"
    headers = {'User-Agent': 'Request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    r_json = response.json()
    hot_posts_json = r_json.get('data').get('children')

    for post in hot_posts_json:
        hot_list.append(post.get('data').get('title'))

    after = r_json.get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
