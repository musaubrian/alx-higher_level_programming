#!/usr/bin/python3
"""
display users github id
#TODO: get id
"""

import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authentization': 'Basic ' + '{}:{}'.format(username, password)}
    headers['Accept'] = 'application/json'
    r = requests.post(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
    else:
        print("None")
