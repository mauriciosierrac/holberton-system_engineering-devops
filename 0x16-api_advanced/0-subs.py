#!/usr/bin/python3
"""How many Subs"""

import requests


def number_of_subscribers(subreddit):
    """[get a parameter of subreddit]
        subreddit: param to argv[1]
    """

    response = requests.get('http://www.reddit.com/r/{}/about.json'.
                            format(subreddit)).json()
    subs = response.get('data', {}).get('subscribers')
    if (subs is None):
        return 0
    return subs
