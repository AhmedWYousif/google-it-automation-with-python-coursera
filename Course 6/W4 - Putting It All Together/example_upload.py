#!/usr/bin/env python3

import requests

# this example shows how a file can be uploaded using python requests module

url = "http://localhost/upload/"
with open("path","r") as opened:
    r = requests.post(url, files={"files":opened})
