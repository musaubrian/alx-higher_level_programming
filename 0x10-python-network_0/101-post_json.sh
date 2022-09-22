#!/bin/bash
# send a POST request with the contents of a file
curl -s -X POST --header 'Content-Type: application/json' --data @"$2" "$1"
