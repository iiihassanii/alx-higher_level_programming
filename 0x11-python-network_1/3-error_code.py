#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)."""
from urllib import request, error
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
