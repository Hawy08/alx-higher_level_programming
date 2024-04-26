#!/usr/bin/python3
import urllib.request
import sys
"""
sends a request to url
displays the value of X-Request-Id variable
"""


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
        