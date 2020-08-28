#! /usr/bin/env python
import os
import requests

directory = "data/feedback"

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename)) as file:
            lines = file.readlines()
            title = lines[0].strip()
            name = lines[1].strip()
            date = lines[2].strip()
            feedback = lines[3].strip()
            data = {"title": title, "name": name, "date": date, "feedback": feedback}
            res = requests.post("http://34.122.122.5/feedback/", data=data)
            print("status_code ",res.status_code)

