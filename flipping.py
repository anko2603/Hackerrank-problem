#You will be given a list of 32 bit unsigned integers. Flip all the bits (1-0) and(0-1) return the result as an unsigned integer.
import math
import os
import random
import re
import sys

def flippingBits(n):
    # Write your code here
   return 2**32 + ~n
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
