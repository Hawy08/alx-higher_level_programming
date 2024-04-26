#!/usr/bin/python3
import requests
import sys
"""
takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response
"""

if __name__ == "__main__":
    reply = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(reply.text)
    