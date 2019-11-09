# STAIRCASE

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = n
    while i > 0:
        space = [" "] * (i - 1)
        stair = ["#"] * (n-i+1)
        spaces = "".join(space)
        stairs = "".join(stair)
        row = spaces + stairs
        print(row)
        i -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
