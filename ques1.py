import math
import os
import random
import re
import sys


def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)