#!/usr/bin/python3
"""
sends a request to the URL 
and displays the value of the X-Request-Id 
"""

from sys import argv
import urllib.request

send_request = urllib.request.Request(argv[1])

with urllib.request.urlopen(send_request) as response:
    headers = response.info()
    print(headers.get('X-Request-Id'))
