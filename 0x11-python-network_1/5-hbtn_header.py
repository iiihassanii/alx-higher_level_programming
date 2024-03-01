#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
the URL and displays the value of the variable 
X-Request-Id in the response header"""
import requests
import sys
url = sys.argv[1]
html = requests.get(url)
print(html.headers.get("X-Request-Id"))
