#!/usr/bin/python3
""" Python script that fetches
https://alx-intranet.hbtn.io/status"""
import requests
html = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(html.text))
print("\t- content:", html.text)
