#!/usr/bin/python3
"""
sends a POST request to the passed URL
with the email as a parameter
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    email_val = {"email": sys.argv[2]}
    email_data = urllib.parse.urlencode(email_val)
    email_data = email_data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], email_data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8", "replace"))
