#!/bin/bash
# script displays the size of the body of the response
size=$(curl -sI "$url" | wc -c); echo "$size"


