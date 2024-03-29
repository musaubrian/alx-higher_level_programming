#!/usr/bin/python3
"""
displays the value of the variable
X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url=url)
    print(req.headers.get("X-Request-Id"))
