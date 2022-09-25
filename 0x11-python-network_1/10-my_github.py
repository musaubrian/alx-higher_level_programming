#!/usr/bin/python3
"""
display users github id
"""

import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    req = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if req.status_code == 200:
        data = req.json()
        print(data.get('id'))
    else:
        print("None")
