#!/bin/bash
#displays the size of the body of the response
curl -sIw '%{size_download}' "$1" | grep "Content-Length:"| cut -d":" -f2

