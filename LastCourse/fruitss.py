#!/usr/bin/env python3

import emails
import reports
from datetime import date
import os
import re

descDir = "./supplier-data/descriptions"
today = date.today()
today = today.strftime("%B %d, %Y")
pattern = r"^(.+)\n([0-9]+ lbs)\n(.+)$"

def getPath(folder):
    listFile = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        listFile.append(path)
    return listFile


def generateParagraph(path):
    with open(path, 'r') as f:
        content = f.readlines()
        string_content = ("").join(content)
        result = re.search(pattern, string_content)
        if result != None:
            return "name: {}<br/>weight: {}<br/>".format(result.group(1), result.group(2))

if __name__ == "__main__":
    pathList = getPath(descDir)
    paraList = []
    for path in pathList:
        paraList.append(generateParagraph(path))
    paragraph = "<br/>".join(paraList)
    reports.generate_report("/tmp/processed.pdf", "Processed Update on {}".format(today), paragraph)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)