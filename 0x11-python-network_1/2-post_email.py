#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(respone.read().decode("utf-8"))
