#There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.Return an array of the results.
import math
import os
import random
import re
import sys
from collections import Counter


def matchingStrings(strings, queries):
    # Write your code here
      s = Counter(strings)
      result=[]
      for q in queries:
        result.append(s[q])
      return result
if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', '/home/ankita/Desktop/Hackerrank-problem/output_file')
    fptr = open(output_path, 'w')


    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()