# Given a time in 12-hour AM/PM format, convert it to military (24-hour) timemNote: - 12:00:00AM on a 12-hour clock is 00:00:00 on a
# 24-hour clock. -12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    if(s[:-2]=="AM" and s[:2]=='12'):
        return "00" + s[2:8]
    elif (s[-2:]=="AM"):
        return s[0:8]
    elif (s[-2:]=="PM"and s[:2=='12']):
        return s[0:8]
    else:
        return str(int(s[0:2])+12)+s[2:8]
    print (timeConversion)
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
   
