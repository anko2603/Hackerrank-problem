#There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    count=0
    d={}
    for i in ar:
        d[i]=d.get(i,0) +1
        
    for i in d.keys():
        count+=d[i]//2
    return count
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
