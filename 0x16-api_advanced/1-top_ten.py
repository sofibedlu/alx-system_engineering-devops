#!/usr/bin/python3
"""request reddit API"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for
    a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'top_ten/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
