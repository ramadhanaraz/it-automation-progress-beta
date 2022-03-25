#!/usr/bin/env python3
import requests
import os
import re

# This example shows how a file can be uploaded using
# The Python Requests module

saveDir = "./supplier-data/images"
url = "http://localhost/upload/"

def getPath(folder):
    listFile = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        isImage = re.search(r".*\.jpeg", path)
        if isImage != None:
            listFile.append(path)
    return listFile

def uploadFiles(path):
    with open(path, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

if __name__ == "__main__":
    pathList = getPath(saveDir)
    for path in pathList:
        uploadFiles(path)
