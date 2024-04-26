#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
"""
takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response
"""

if __name__ == "__main__":
    info = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(info)
    url = sys.argv[1]
    reply = urllib.request.Request(url, data)
    with urllib.request.urlopen(reply) as response:
        body = response.read()
    print(body.decode(encoding="utf-8"))
        