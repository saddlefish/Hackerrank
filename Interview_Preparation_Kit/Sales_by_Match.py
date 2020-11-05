import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_dict = {}
    for i in ar:
        if i not in color_dict:
            color_dict[i]=1
            continue
        #else:    
        color_dict[i]+=1
    pair_count = 0 
    
    for i in color_dict.values():
        pair_count += i//2
    return pair_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
