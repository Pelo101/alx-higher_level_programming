#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -X  OPTIONS -I -L $1 | grep "Allow"
