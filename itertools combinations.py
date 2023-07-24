"""
This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
"""

from itertools import *

S, k = input().split()
k = int(k)
for i in range(1, k+1):
    for d in combinations(sorted(S), i):
        print("".join(d))
