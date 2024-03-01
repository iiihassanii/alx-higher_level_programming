#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, passwd))
    if response.json != '{}':
        user_id = response.json().get('id')
    else:
        print(None)
