#!/usr/bin/env python

import os
import re
import requests

fileDir = "review"
pattern = r"^(.+)\n(.+)\n([0-9\-]+)\n(.+)$"


def getPath(folder):
    listFile = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        listFile.append(path)
    return listFile


def generateDictionary(path):
    dictContent = {}
    with open(path, 'r') as f:
        content = f.readlines()
        string_content = ("").join(content)
        result = re.search(pattern, string_content)
        if result != None:
            dictContent['title'] = result.group(1)
            dictContent['name'] = result.group(2)
            dictContent['date'] = result.group(3)
            dictContent['feedback'] = result.group(4)
    return dictContent


if __name__ == "__main__":
    reqList = []
    pathList = getPath(fileDir)
    for path in pathList:
        reqList.append(generateDictionary(path))
    for review in reqList:
        response = requests.post(
            "http://35.222.103.215/feedback/", data=review)
        response.raise_for_status()
