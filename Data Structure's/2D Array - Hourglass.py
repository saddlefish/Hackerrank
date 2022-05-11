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
    """
    There are two solutions I wrote below, the first one takes less code writing, however,
    they both achieve the same outcome
    """
    # Write your code here
    ans = -math.inf
    for row in range(4):
        for col in range(4):
            #solution 1 
            top_sum = sum(arr[row][col:col+3])
            mid_sum = arr[row+1][col+1]
            bot_sum = sum(arr[row+2][col:col+3])
            total = top_sum + mid_sum + bot_sum
            
            if total > ans:
                ans = total
    return ans
    
    #solution 2
    #        hourglass_sum = arr[row][col] + arr[row][col+1] + arr[row][col+2] + \
    #        arr[row+1][col+1] + \
    #        arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
    #        ans = max((ans, hourglass_sum))
    #return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
