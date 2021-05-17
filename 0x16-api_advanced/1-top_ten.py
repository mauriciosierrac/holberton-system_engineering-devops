#!/usr/bin/python3
"""Top Ten
"""

import requests


def top_ten(subreddit):
    """Write a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit ([string]): [from 1-main / argv[1]]
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    params = {
        "limit": 10
    }

    response = requests.get(url, params=params)
    if (response is None):
        print('None')
        return
    res = response.json()
    result = res.get('data').get('children')
    for i in result:
        respo = i.get('data').get('title')
        print(respo)
