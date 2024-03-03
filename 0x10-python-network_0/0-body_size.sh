#!/bin/bash
#  a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -i $1 2>/dev/null| grep Content-Length | awk '{print $2}'
