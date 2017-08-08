#!/usr/bin/python

from sets import Set

title = open("./title", "r")

encoding = {}
lines = title.readlines()
title.close()

for i in range(len(lines)):
    part2 = lines[i].strip("\r\n").split(":")[1].strip(" .")
    if part2 == "continuous":
        continue
    encoding[i] = {}
    elems = part2.split(",")
    for j in range(len(elems)):
        code = [0]*len(elems)
        code[j] = 1
        encoding[i][elems[j].strip(" ")] = code
    encoding[i]["?"] = [0]*len(elems)

data = open("./adult.data", "r")

while True:
    line = data.readline()
    if not line:
        break
    elems = line.strip("\r\n").split(",")
    newline = ""
    for i in range(len(elems)):
        if not encoding.has_key(i):
            newline = newline + "," + elems[i]
            continue
        elem = elems[i].strip(" ")
        for v in encoding[i][elem]:
            newline = newline + ", " + str(v)
    print newline.strip(",")

data.close()
