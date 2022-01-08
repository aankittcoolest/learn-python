import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    hops = 0
    y = 0
    while y < len(c):
        if y + 2 <= len(c) - 1 and c[y + 2] == 0:
            hops += 1
            y = y + 2
            continue
        elif y + 1 <= len(c) - 1 and c[y + 1] == 0:
            hops += 1
            y = y + 1
            continue
        else:
            break
    return hops


if __name__ == '__main__':
    jumpingOnClouds([0, 1, 0, 0, 0, 1, 0])
