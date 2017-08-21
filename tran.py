#!/usr/bin/python

from numpy import *

Yarr = []
Xarr = []

data = open("./adult.data.onehot", "r")

while True:
    line = data.readline()
    if not line:
        break
    elems = line.strip("\r\n").split(",")
    xi = [1]*(len(elems))
    for i in range(len(elems)-1):
        xi[i] = int(elems[i].strip(" "))
    Xarr.append(xi)

    res = elems[len(elems)-1].strip(" ")
    if res == "<=50K":
        Yarr.append([0])
    else:
        Yarr.append([1])

data.close()

X = array(Xarr)
Y = array(Yarr)

A = dot(X.T, X)
B = dot(X.T, Y)
W = linalg.pinv(A).dot(B)

savetxt("./w", W, fmt="%.8f", delimiter=",")
