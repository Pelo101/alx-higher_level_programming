#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""
import urllib.request

url = "https://alx-intranet.hbtn.io"
with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader("x-request-id")
    print(x_request_id)
