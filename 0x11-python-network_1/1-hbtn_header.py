#!/usr/bin/python3
""" Python script that takes displays x-request-id"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers
    x_request_id = headers.get("X-Request-Id")
    print(x_request_id)
