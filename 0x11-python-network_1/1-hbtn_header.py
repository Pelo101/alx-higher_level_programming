#!/usr/bin/python3
""" Python script that takes displays x-request-id"""
import urllib.request

url = "https://alx-intranet.hbtn.io"
with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader("x-request-id")
    print(x_request_id)
