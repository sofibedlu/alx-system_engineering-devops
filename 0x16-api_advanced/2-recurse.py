#!/usr/bin/python3
"""retrieve a data recurssively"""

import requests


def recurse(subreddit, after=None, hot_list=[]):
    """returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'recurse/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        next_page = data['data']['after']

        if next_page:
            return recurse(subreddit, next_page, hot_list)
        else:
            return hot_list
    else:
        return None
