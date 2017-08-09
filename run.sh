#!/bin/bash

./onehot.py ./adult.data > adult.data.onehot
./tran.py
./onehot.py ./adult.test > adult.test.onehot
./test.py > result
