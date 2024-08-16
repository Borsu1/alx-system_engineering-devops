#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after='', word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the titles.
        after (str, optional): The 'after' parameter for pagination.
            Defaults to ''.
        word_count (dict, optional): A dictionary to store the count
            of keywords. Defaults to None.

    Returns:
        None: Prints the sorted count of keywords in descending order.
    """
    if word_count is None:
        word_count = {}

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (
        f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    )
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException as e:
        return

    try:
        data = response.json().get('data', {})
    except ValueError as e:
        return

    after = data.get('after', None)
    posts = data.get('children', [])

    for post in posts:
        title_words = post['data']['title'].lower().split()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(
                    word_lower, 0) + title_words.count(word_lower)

    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f'{word}: {count}')

# Example usage
    count_words('python', ['python', 'java', 'javascript', 'react'])
