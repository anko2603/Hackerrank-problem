# HackerLand University has the following grading policy: Every student receives a grade in the inclusive range from 0 to 100.Any grade less
# than 40 is a failing grade.Sam is a professor at the university and likes to round each student's grade according to these rules:If the 
# difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.If the value of grade  is 
# less than 38, no rounding occurs as the result will still be a failing grade.
import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    ans=[]
    for grade in grades:
        if grade<38:
            ans.append(grade)
        elif grade%5>2:
            grade= (grade//5+1)*5
            ans.append(grade)
        else:
            ans.append(grade)
    return ans

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.text')
    fptr = open(output_path, 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
