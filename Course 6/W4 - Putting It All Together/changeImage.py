#!/usr/bin/env python3

from PIL import Image
import os

directory = "supplier-data/images"
output_directory = "supplier-data/images"
for filename in os.listdir(directory):
    if filename.endswith(".tiff"):
        im = Image.open(os.path.join(directory, filename))
        im = im.convert("RGB")
        im = im.resize((600,400))
        im.save(os.path.join(output_directory, filename.split(".")[0] + ".jpeg"))