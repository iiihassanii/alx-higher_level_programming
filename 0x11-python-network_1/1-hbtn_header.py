#!/usr/bin/python3
from urllib import request
import sys
"""Python script that takes
in a URL, sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response."""


url = sys.argv[1]
with request.urlopen(url) as response:
    item = response.headers.get('X-Request-Id')
    if item:
        print(item)
