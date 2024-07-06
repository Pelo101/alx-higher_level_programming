#!/usr/bin/python3
""" Python script that takes your GitHub credentials"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    username, access_token = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, access_token))

    print(response.json().get('id'))
