#!/bin/bash
#display all http methods allowed
curl -sI "$1" | grep Allow | cut -d" " -f2-
