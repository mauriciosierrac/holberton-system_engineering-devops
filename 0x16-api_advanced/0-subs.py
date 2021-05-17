#!/usr/bin/python3
"""How many Subs"""

import requests


def number_of_subscribers(subreddit):
    """[get a parameter of subreddit]
        subreddit: param to argv[1]
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {
        "User-Agent": "linux:task00.api:v1.0.0 (by /u/Holberton2020)"
    }

    response = requests.get(url, headers=headers)

    if (response.status_code == 404):
        return 0
    res = response.json().get('data', {}).get('suscribers', 0)
    return res
