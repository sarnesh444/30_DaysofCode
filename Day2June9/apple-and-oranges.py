import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #s-start point of sams house
    #t-end point of sams house
    #a-apple tree point
    #b-orange tree point 
    resapples=[(i+a) for i in apples if(i+a) in range(s,t+1) ]
    resoranges=[(i+b) for i in oranges if(i+b) in range(s,t+1)]
    print(len(resapples))
    print(len(resoranges))
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
