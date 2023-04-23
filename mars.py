# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.Letters in some of the 
# SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string,s, determine
# how many letters of the SOS message have been changed by radiation.
import math
import os
import random
import re
import sys

def marsExploration(s):
    # Write your code here
    count=0
    r = len(s)//3
    target="SOS"*r
    for i,j in zip (s,target):
        if i != j:
          count+=1
    return count 
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
