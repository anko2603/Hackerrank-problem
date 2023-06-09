#Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
import math
import os
import random
import re
import sys
from collections import Counter

def pickingNumbers(a):
    # Write your code here
    arr = Counter(a)
    maxnum = 0
    for i in range(100):
        maxnum = max(maxnum,arr[i]+arr[i+1])
    return maxnum


if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()