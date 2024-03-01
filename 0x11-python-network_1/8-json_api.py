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

    try:
        response = requests.post(
            'http://0.0.0.0:5000/search_user', data=values)
        json_response = response.json()

        if "id" in json_response and "name" in json_response:
            print("[{}] {}".format(json_response.get(
                "id"), json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
