#Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.Lily decides to share a contiguous 
#segment of the bar selected such that:The length of the segment matches Ron's birth month, and,The sum of the integers on the squares is 
#equal to his birth day.Determine how many ways she can divide the chocolate.
import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count=0
    total=sum(s[:m])
    if total ==d:
        count+=1
    for i in range(m,len(s)):
        total+=s[i]
        total-=s[i-m]
        if total ==d:
            count+=1
    return count

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')
    
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
