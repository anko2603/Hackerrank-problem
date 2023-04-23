#There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that the relation A'[i]+B'[i]>_k holds for all i where 0<_i<n There will be q queries consisting of A,B, and k. For each query, return YES if some permutation A',B'  satisfying the relation exists. Otherwise, return NO.
import math
import os
import random
import re
import sys

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    for i in range (len(A)):
        if A[i]+B[i]<k:
            return "NO"
    return "YES"    
    
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()