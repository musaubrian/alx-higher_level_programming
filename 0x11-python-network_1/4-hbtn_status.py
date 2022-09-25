#!/usr/bin/python3
"""
use request package to get response
"""
import requests
url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    req = requests.get(url)
    response = req.text
    print("Body response")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
