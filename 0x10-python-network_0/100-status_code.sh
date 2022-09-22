#!/bin/bash
#get a response
curl -s -o /dev/null -w "%{http_code}" "$1"
