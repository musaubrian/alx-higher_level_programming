#!/bin/bash
#displays body size of requested url
curl -sIw '%{size_download}' "$1" | grep "Content-Length:"| cut -d":" -f2
