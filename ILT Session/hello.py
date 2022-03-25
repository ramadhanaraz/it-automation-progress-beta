#!/usr/bin/env python

data = input("This will come from STDIN: ")
print("Now we will write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
