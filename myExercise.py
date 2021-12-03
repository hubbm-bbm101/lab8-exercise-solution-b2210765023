import sys

file = open(sys.argv[1], "r").read().splitlines()
commands = sys.argv[2].split(",")
data = {}

for i in file:
    student , info = i.split(":")
    data[student] = info.split(",")

for i in commands:
    try:
        data[i]
        print(f"Name: {i}")
        print(f"University: {(',').join(data[i])}")
    except Exception:
        print(f"No record of {i} was found!")
