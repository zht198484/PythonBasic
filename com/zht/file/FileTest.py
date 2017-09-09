import os

print os.getcwd()

os.chdir("../../../")

print os.getcwd()

with open("111.txt") as lines:
    for line in lines:
        print line
