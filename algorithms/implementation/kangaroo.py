#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if v2 == v1:
        return 'NO'
    
    steps = (x1-x2)/(v2-v1)
    
    if steps < 0 or steps%1 > 0:
        return 'NO'
    else:
        return 'YES'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
