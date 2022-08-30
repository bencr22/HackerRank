#!/bin/python3


def miniMaxSum(arr):
    arr.sort()
    
    large_sum = sum(arr[-4:])
    small_sum = sum(arr[:4])
    print(small_sum, large_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
