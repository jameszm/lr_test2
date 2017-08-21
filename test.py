#!/usr/bin/python

from numpy import *
from sklearn.metrics import roc_auc_score

W = loadtxt("./w")

Yarr = []
Xarr = []

data = open("./adult.test.onehot", "r")

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

Y2 = dot(X, W)

auc = roc_auc_score(Y, Y2)
print "AUC:", auc
