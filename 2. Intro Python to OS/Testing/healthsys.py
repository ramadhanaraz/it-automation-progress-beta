import psutil
import shutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free / du.total)*100
    return free > 20


def check_cpu_usage(time):
    usage = psutil.cpu_percent(time)
    return usage < 75


if not check_disk_usage("C:\\") or not check_cpu_usage(1):
    print("ERROR!")
else:
    print("Everything is OK!")