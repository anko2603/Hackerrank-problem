#Given an array of integers, where all elements but one occur twice, find the unique element.
import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Write your code here
    result = 0
    for num in a:
        result ^= num
    return result
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
