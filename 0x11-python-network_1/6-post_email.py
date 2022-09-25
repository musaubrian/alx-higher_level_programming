#!/usr/bin/python3
"""
sends a POST request
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email_val = {"email": sys.argv[2]}
    req = requests.post(url=url, data=email_val)
