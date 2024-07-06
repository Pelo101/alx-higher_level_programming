#!/usr/bin/python3
""" Python script that takes your GitHub credentials"""

import sys
import requests

if __name__ == "__main__":
    username, access_token = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, access_token))

    if response.status_code == 200:
        user_data = response.json()
        print(f"User ID: {user_data['id']}")
    else:
        print(f"failed user informaton.{response.status_code}")
