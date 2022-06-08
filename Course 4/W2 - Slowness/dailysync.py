#!/usr/bin/env python

import subprocess
from multiprocessing import Pool
import os

def copy(args):
    # Do something with task here
    print("Handling {} {}".format(args[0],args[1]))
    subprocess.call(["rsync", "-arq", args[0], args[1]])

if __name__ == "__main__":
    src = "/data/prod/"
    dest = "/data/prod_backup/"

    tasks = []
    for root, dirs, files in os.walk(src, topdown=False):
        for name in dirs:
            tasks.append([os.path.join(root, name),os.path.join(dest, name)])
    print(tasks)
    p = Pool(len(tasks))
    p.map(copy, tasks)

    

    ###################################################
#try this 
#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess

src = "/home/student-03-#######/data/prod"
dirs = next(os.walk(src))[1]

def backingup(dirs):
    dest = "/home/student-03-#######/data/prod_backup"
    subprocess.call(["rsync", "-arq", src+'/'+ dirs, dest])




p = Pool(len(dirs))
p.map(backingup, dirs)
