# Quicksort usually has a running time of n*log(n), but is there an algorithm that can sort even faster? In general, this is not possible. 
# Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm 
# cannot beat n*log(n)(worst-case) running time, since n*log(n)represents the minimum number of comparisons needed to know where to place each element.
import math
import os
import random
import re
import sys

def countingSort(arr):
    # Write your code here
    count=[0]*100
    for num in arr:
        count[num]+=1
    return count    

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
