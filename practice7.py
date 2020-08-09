#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    msg = s.split(' ') 
    msg1 = ""
    for x in range(0,len(msg)):
        if x==0:
            msg1 =  msg1 +  msg[x].capitalize() 
        else:
            msg1 = msg1 + ' ' + msg[x].capitalize()       
    return msg1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print((str(result) + '\n'))
    #fptr.write(result + '\n')

   # fptr.close()
