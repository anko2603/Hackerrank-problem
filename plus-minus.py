#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
import math
import os
import random
import re
import sys
def plusMinus(arr):
    # Write your code here
    positive_count=0
    negative_count=0
    zero_count=0
    for num in arr:
        if num>0:
            positive_count +=1
        elif num<0:
            negative_count +=1
        else:
            zero_count +=1
    total=len(arr)
    positive_ratio=positive_count/total
    negative_ratio=negative_count/total
    zero_ratio=zero_count/total
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio)) 
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
