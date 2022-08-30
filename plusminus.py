#!/bin/python3

import numpy as np


def plusMinus(arr, n):
    # get the proportion of each element
    positive_prop = len(list(filter(lambda y: (y > 0), arr))) / n
    negative_prop = len(list(filter(lambda x: (x < 0), arr))) / n
    zero_prop = arr.count(0) / n

    # format for output
    print("%.5f" %positive_prop)
    print("%.5f" %negative_prop)
    print("%.5f" %zero_prop)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
