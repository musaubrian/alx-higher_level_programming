#!/usr/bin/python3
"""
send a POST request to search for a user
"""

import sys
import requests

if __name__ == "__main__":
    to_search = ""
    if len(sys.argv[1]) > 1:
        to_search = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url=url, data={"q": to_search})

    try:
        json_resp = req.json()
        if not json_resp:
            print("No result")
        else:
            print(f"[{json_resp.get('id')}] {json_resp.get('name')}")
    except requests.exceptions.JSONDecodeError as not_json:
        print("Not a valid json")
