#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    data = ""
    if len(sys.argv) == 2:
        data = sys.argv[1]
    print(data)
    values = {"q": data}
    response = requests.post(
        'http://0.0.0.0:5000/search_user', data=values)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
