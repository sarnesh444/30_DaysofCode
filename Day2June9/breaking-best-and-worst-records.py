import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    countmax,countmin=0,0
    maxval,minval=scores[0],scores[0]
    for i in scores:
        if(i>maxval):
            maxval=i
            countmax+=1
        if(i<minval):
            minval=i
            countmin+=1
    return countmax,countmin

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(*result)
