import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    m1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    m2 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    m4 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    m5 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    m6 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    m7 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    m8 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    return min(diff(s, m1), diff(s, m2), diff(s, m3), diff(s, m4), diff(s, m5), diff(s, m6), diff(s, m7), diff(s, m8))
    # Write your code here


def diff(s, m):
    d = abs(s[0][0] - m[0][0]) + abs(s[0][1] - m[0][1]) + abs(s[0][2] - m[0][2]) + abs(s[1][0] - m[1][0]) + abs(
        s[1][1] - m[1][1]) + abs(s[1][2] - m[1][2]) + abs(s[2][0] - m[2][0]) + abs(s[2][1] - m[2][1]) + abs(
        s[2][2] - m[2][2])
    print(d)
    return d


if __name__ == '__main__':
    # output = formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])
    output = formingMagicSquare([[4, 9, 2], [9, 7, 6], [3, 5, 8]])
    print(output)

# 2 7 6   # 6 7 2   # 8 1 6   # 6 8 1
# 9 5 1   # 1 5 9   # 3 5 7   # 7 3 5
# 4 3 8   # 8 3 4   # 4 9 2   # 2 4 9

# 4 3 8   # 8 3 4   # 4 9 2   # 2 4 9
# 9 5 1   # 1 5 9   # 3 5 7   # 7 3 5
# 2 7 6   # 6 7 2   # 8 1 6   # 6 8 1


# [[4, 9, 2], [9, 7, 6], [3, 5, 8]]
# [[6, 8, 1], [7, 3, 5], [2, 4, 9]]

# 2 1 1 2 4 1 1 1 1

