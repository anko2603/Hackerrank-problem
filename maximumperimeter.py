#VGiven an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. Return an array of the lengths of its sides as 3 integers in non-decreasing order.If there are several valid triangles having the maximum perimeter:Choose the one with the longest maximum side.If more than one has that maximum, choose from them the one with the longest minimum side.If more than one has that maximum as well, print any one them.If no non-degenerate triangle exists, return[-1] .
import math
import os
import random
import re
import sys

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    i=len(sticks)-3
    while i >=0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
        i-=1
    if i>=0:
        return [sticks[i],sticks[i+1],sticks[i+2]]
    else:
        return [-1]

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')


    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()