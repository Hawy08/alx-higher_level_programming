#!/usr/bin/python3

import requests
import sys
"""
sends a request to url
displays the value of X-Request-Id variable
"""


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.header.get('X-Request-Id'))
        