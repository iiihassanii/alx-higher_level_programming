#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    data = ""
    if sys.argv[1]:
        data = sys.argv[1]
    values = {"q": data}

    response = requests.post('http://0.0.0.0:5000/search_user', data=values)

    try:
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
