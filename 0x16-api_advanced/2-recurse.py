#!/usr/bin/python3
""" Recurse it! """

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Write a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit ([string]): [argv[1]]
        hot_list (list, optional): [parameter]. Defaults to [].
        after (str, optional): [parameter]. Defaults to "".
        count (int, optional): [parameter]. Defaults to 0.

    Returns:
        [type]: [description]
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:task00.api:v1.0.0 (by /u/Holberton2020)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
