#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o - "$1" | grep -q  "Route 1" && echo "Route 2"

