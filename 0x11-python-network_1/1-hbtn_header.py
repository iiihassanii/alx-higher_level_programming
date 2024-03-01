#!/usr/bin/python3
from urllib import request
import sys
"""Python script that takes
in a URL, sends a request to the URL"""
with request.urlopen(sys.argv[1]) as response:
    item = response.headers.get('X-Request-Id')
    print(item)
