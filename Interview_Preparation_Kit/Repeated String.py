import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    stringDiv = (n // len(s))
    count = s.count('a')
    if n % len(s) == 0:
        count = count * stringDiv
    else:
        alt_choice = (n%len(s))
        count = count * stringDiv + s[:alt_choice].count('a')
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
