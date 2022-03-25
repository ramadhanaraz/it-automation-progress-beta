#!/usr/bin/env python

import os
import re
import requests

descDir = "./supplier-data/descriptions"
pattern = r"^(.+)\n([0-9]+) lbs\n(.+)$"


def getPath(folder):
    listFile = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        listFile.append(path)
    return listFile


def generateDictionary(path):
    fileName = os.path.splitext(os.path.basename(path))[0]
    dictContent = {}
    with open(path, 'r') as f:
        content = f.readlines()
        string_content = ("").join(content)
        result = re.search(pattern, string_content)
        if result != None:
            dictContent['name'] = result.group(1)
            dictContent['weight'] = int(result.group(2))
            dictContent['description'] = result.group(3)
            dictContent['image_name'] = "{}.jpeg".format(fileName)
    return dictContent


if __name__ == "__main__":
    reqList = []
    pathList = getPath(descDir)
    for path in pathList:
        reqList.append(generateDictionary(path))
    for catalogue in reqList:
        response = requests.post(
            "http://34.66.102.157/fruits/", data=catalogue)
        response.raise_for_status()
