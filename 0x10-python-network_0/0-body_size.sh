#!/bin/bash
# script displays the size of the body of the response
curl -sL "$1" | awk '/Content-Length/ {print $2}'; echo -n 
