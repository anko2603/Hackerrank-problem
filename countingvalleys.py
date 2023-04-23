# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, for every step it was noted if 
# it was an uphill,U , or a downhill,Dstep. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude.
# We define the following terms:A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with 
# a step down to sea level.A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a
# step up to sea level.Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    valleycount=level=0
    d={'U':1,'D':-1}
    for step in path:
        level += d[step]
        if level ==0 and step =='U':
            valleycount+=1
    return valleycount
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
