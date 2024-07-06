#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to url"""

import sys
import requests

if __name__ == "__main__":
    
    url = 'http://0.0.0.0:5000/search_user' 

    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': letter}

    response = requests.post(url, data=payload)

    json_data = response.json()

    try:
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not valid JSON")
