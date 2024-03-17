#!/usr/bin/python3
"""A script that
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == '__main__':

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json = r.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))

    except ValueError:
        print("Not a valid JSON")
