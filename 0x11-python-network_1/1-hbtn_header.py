#!/usr/bin/python3
import urllib.request
import sys
"""Python script that takes
in a URL, sends a request to the URL"""
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        item = response.headers.get('X-Request-Id')
        print(item)
