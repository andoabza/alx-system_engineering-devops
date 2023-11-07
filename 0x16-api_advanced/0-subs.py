#!/usr/bin/python3
""" a scriptthat return the number of subscriber of reedit"""
import requests

def number_of_subscribers(subreddit):
    """a function that return number of subscribersd"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'anda'}  # Set a custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
