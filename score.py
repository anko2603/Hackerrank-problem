#Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of 
#times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record
#for the season, and she begins counting from there.
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # Write your code here
    maxcount=mincount=0
    maxscore=minscore=scores[0]
    for i in range(1,len(scores)):
        if minscore<scores[i]:
           minscore=scores[i]
           mincount+=1
        elif maxscore>scores[i]:
            maxscore=scores[i]
            maxcount+=1
    return  mincount,maxcount
        
        

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
