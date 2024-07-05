#!/usr/bin/python3
""" Python script that displays the value of the variable X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-ID")
    print(x_request_id)
