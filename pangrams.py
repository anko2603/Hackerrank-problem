#A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
import math
import os
import random
import re
import sys

def pangrams(s):
    # Write your code here
    temp = set(s.lower()) - set(' ')
    
    if len(temp)== 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
