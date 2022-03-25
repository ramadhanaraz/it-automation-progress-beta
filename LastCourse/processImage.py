#!/usr/bin/env python3

import os
import re
from PIL import Image

saveDir = "opticons"


def getPath(folder):
    listFile = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        isImage = re.search(r".*\.DS_Store", path)
        if isImage == None:
            listFile.append(path)
    return listFile


def processImage(path):
    im = Image.open(path)
    fileName = re.search(r".*\/(.+)", path)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    im.rotate(90).resize((128, 128)).save(
        os.path.join(saveDir, fileName.group(1)+".jpeg"))


if __name__ == "__main__":
    pathList = getPath("images")
    for path in pathList:
        processImage(path)
