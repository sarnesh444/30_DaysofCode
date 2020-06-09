import math
import os
import random
import re
import sys
from collections import Counter
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d=Counter(arr)
    di=dict(d)
    return max(di, key= lambda x: di[x])

if __name__ == '__main__':
    

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
