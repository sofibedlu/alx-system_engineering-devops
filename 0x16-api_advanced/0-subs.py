#!/usr/bin/python3
"""request reddit API"""

import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'subs/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        res_json = response.json()
        sub_count = res_json['data']['subscribers']
        return sub_count
    else:
        return 0
