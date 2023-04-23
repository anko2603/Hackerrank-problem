# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum=sum(arr[0:4])
    max_sum=sum(arr[1:5])
    print(min_sum,max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
