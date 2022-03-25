#!/usr/bin/env python3

import re
import operator

pattern = r" ticky: ([A-Z]+) (.+) \((\w+)\)"
per_user = {}
error = {}

with open("syslog.log", "r") as f:
    for line in f.readlines():
        match = re.search(pattern, line.strip('\n'))
        if match == None:
            continue
        if not match.group(3) in per_user:
            per_user[match.group(3)] = [0,0]
        if match.group(1) == "ERROR":
            per_user[match.group(3)][1] += 1
            if not match.group(2) in error:
                error[match.group(2)] = 0
            error[match.group(2)] += 1
        if match.group(1) == "INFO":
            per_user[match.group(3)][0] += 1
    sorted_per_user = sorted(per_user.items(), key = operator.itemgetter(0), reverse=False)
    sorted_error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)

with open("error_message.csv", "w") as f:
    f.write("Error, Count" + "\n")
    for error, count in sorted_error:
        f.write("{}, {}".format(error, count) + "\n")

with open("user_statistics.csv", "w") as f:
    f.write("Username, INFO, ERROR" + "\n")
    for user, count in sorted_per_user:
        f.write("{}, {}, {}".format(user, count[0], count[1]) + "\n")
