#!/usr/bin/python3
"""
handle HTTP errors
"""

import sys
import urllib.error
import urllib.request
import urllib.parse

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except Exception as e:
        print(f'Error code: {e.code}')
