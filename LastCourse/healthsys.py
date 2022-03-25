#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails
import os

def check_disk_usage():
    du = shutil.disk_usage()
    free = (du.free / du.total)*100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent()
    return usage < 80


def check_mem_usage():
    availableMem = psutil.virtual_memory().available / (1024.0 ** 2)
    return availableMem > 500

def check_connection():
    sock = socket.socket()
    address = '127.0.0.1'
    port = 80
    try:
        sock.connect(address, port)
    except Exception as e:
        return -1
    
def errorType():
    if not check_cpu_usage():
        return "Error - CPU usage is over 80%"
    elif not check_disk_usage():
        return "Error - Available disk space is less than 20%"
    elif not check_mem_usage():
        return "Error - Available memory is less than 500MB"
    elif check_connection() == -1:
        return "Error - localhost cannot be resolved to 127.0.0.1"

if __name__ == "__main__":  
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = errorType()
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error(sender, receiver, subject, body)
    emails.send_email(message)