#! /usr/bin/env python3

import os
import requests


directory = "supplier-data/descriptions"
upload_url = "http://localhost/fruits/"

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename)) as opened:
            lines = opened.readlines()
            name = lines[0].strip()
            weight = int(lines[1].strip().replace(" lbs",""))
            description = lines[2].strip()
            image_name = filename.split(".")[0] + ".jpeg"
            data = {"name": name, "weight": weight, "description": description, "image_name": image_name}
            res = requests.post(upload_url, data=data)
            print("status_code ",res.status_code)
