import os
work_file = os.path.join(os.path.dirname(__file__), 'tz', "example.txt")

with open(work_file, "r") as file:
    print(file.read())