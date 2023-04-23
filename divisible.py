#Given an array of integers and a positive integer , determine the number of(i,j)  pairs where i<j and ar[i]+ ar[j] is divisible by k .
import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(i+1,n): 
            if (ar[i]+ar[j]) %k == 0:
                count +=1
    return count
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
