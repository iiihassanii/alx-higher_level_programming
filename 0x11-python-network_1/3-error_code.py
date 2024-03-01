#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)."""
from urllib import request, parse, error
import sys
url = sys.argv[1]
try:
    response = request.urlopen(url)
    print(response.read().decode('utf-8'))
except error.URLError as e:
    print("Error code: ", e.code)
