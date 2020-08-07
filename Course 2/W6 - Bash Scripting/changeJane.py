#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
    lines = file.readlines()
    for line in lines:
        oldvalue = line.strip()
        newvalue = oldvalue.replace("jane", "jdoe")
        subprocess.run(["mv", oldvalue, newvalue])
file.close()