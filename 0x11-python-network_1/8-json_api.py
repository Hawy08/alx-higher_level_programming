#!/usr/bin/python3
import requests
from sys import argv
"""
Script that takes a letter and post request to url/search_user
"""


if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q}).json()
        if 'id' in response and 'name' in response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
        