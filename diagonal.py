#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    d1=d2=0
    for i in range(n):
        d1+=arr[i][i]
        d2+=arr[i][n-i-1]
        dif=abs(d1-d2)
    return (dif)
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
