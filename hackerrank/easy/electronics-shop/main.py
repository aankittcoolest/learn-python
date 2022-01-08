import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    m = -1
    for x in keyboards:
        for y in drives:
            if b >= x + y > m:
                m = x + y
    return m

if __name__ == '__main__':
    getMoneySpent([3,1],[5,2,8],10)
