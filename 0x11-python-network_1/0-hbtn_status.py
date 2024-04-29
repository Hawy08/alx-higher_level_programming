#!/usr/bin/python3
import urllib.request

"""
Script that fetches the status of the Alx Intranet website and prints information about the response.

This script utilizes the urllib.request module to make an HTTP GET request to the URL https://alx-intranet.hbtn.io/status.
It then retrieves the response body and prints information about it, including the type of the response body, the raw content,
and the decoded content assuming it is encoded in UTF-8.
"""

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode(encoding="utf-8")))
