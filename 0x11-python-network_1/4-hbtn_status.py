#!/usr/bin/python3

import requests

"""
script that fetches https://alx-intranet.hbtn.io/status
"""   

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    