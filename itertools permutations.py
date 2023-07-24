"""
This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""
from itertools import *

#S = ()
S = input().split()
for i in permutations(sorted(S[0]), int(S[1])):
    print("".join(i))
