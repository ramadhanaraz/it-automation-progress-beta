
#!/usr/bin/env python
import os
import subprocess
from multiprocessing import Pool

src = "/home/student-00-554c3c4d744d/data/prod/"
dest = "/home/student-00-554c3c4d744d/data/prod_backup/"

def generate_pathlist(dir):
    pathlist = []
    for root, dirs, files in os.walk(dir):
        path = root[len(dir):]
        for name in files:
            pathlist.append((path, name))
        for name in dirs:
            pathlist.append((path, name))
    return pathlist

def run(path):
    # Do something with task here
    rsync_src = os.path.join(src, path[0], path[1])
    rsync_dest = os.path.join(dest, path[0])
    subprocess.call(['rsync', '-arq', rsync_src, rsync_dest])

if __name__ == "__main__":
    # Create a pool of specific number of CPUs
    pathlist = generate_pathlist(src)
    # Start each task within the pool
    p = Pool(len(pathlist))
    p.map(run, pathlist)