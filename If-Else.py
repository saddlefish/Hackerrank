import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #if n is odd print weird
    if n % 2 != 0:
        print("Weird")
    else:
        #if n is even and in range 2-5
        if(n>=2 and 5<=n):
            print("Not Weird")
        #if n is even and in range 6-20
        elif(n>=6 and 20<=n):
            print("Weird")
        #if n is greater than 20    
        elif(n>20):
            print("Not Weird")
