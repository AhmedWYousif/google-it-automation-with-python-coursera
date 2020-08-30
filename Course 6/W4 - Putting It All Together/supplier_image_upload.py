#!/usr/bin/env python3

import requests
import os

directory = "supplier-data/images"
upload_url = "http://localhost/upload/"

for filename in os.listdir(directory):
    if filename.endswith(".jpeg"):
        with open(os.path.join(directory, filename),"rb") as opened:
            r = requests.post(upload_url, files={"file":opened})
            print(r.status_code)
