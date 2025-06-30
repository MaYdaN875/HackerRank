#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    clockSum = []
    
    for i in range(4):                   #Cantidad de filas
        for j in range(4):
            s = arr[i][j]                   #[0][0]
            s+= arr[i][j+1]                 #[0][1]
            s+= arr[i][j+2]                 #[0][2]
            s+= arr[i+1][j+1]               #[1][1]
            s+= arr[i+2][j]                 #[2][0]
            s+= arr[i+2][j+1]               #[2][1]
            s+= arr[i+2][j+2]               #[2][2]
            clockSum.append(s)
    
    clockSum.sort()
    return clockSum[len(clockSum)-1]            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
