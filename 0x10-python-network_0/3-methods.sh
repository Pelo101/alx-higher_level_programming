#!/bin/bash
# Bash script that displays all HTTP methods the server will accept.
curl -sI "$1" | grep "ALLOW" | cut -d ' ' -f2-
