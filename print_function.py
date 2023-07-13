"""
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following: 123...n

Note that ""..."" represents the consecutive values in between.

example: n = 5, print string 12345
"""

if __name__ == '__main__':
    n = int(input())
    i = 0 
    while i < n:
        i = i + 1
        print(i, end="")
