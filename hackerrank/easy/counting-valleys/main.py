import math
import os
import random
import re
import sys
from collections import deque
from queue import LifoQueue


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    x = list(path)
    stack = []
    count = 0
    for a in x:
        if len(stack) == 0 and a == 'D':
            count += 1
            stack.append(a)
        elif len(stack) > 0 and stack[len(stack)-1] != a:
            stack.pop()
        else:
            stack.append(a)
    return count

if __name__ == '__main__':
    countingValleys(8, "UDDDUDUU")
    countingValleys(8, "DDUUUUDD")
