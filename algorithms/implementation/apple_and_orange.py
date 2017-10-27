#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

a_count = 0
o_count = 0

for apple_dist in apple:
    apple_loc = a + apple_dist
    if apple_loc >= s and apple_loc <= t:
        a_count +=1

for orange_dist in orange:
    orange_loc = b + orange_dist
    if orange_loc <= t and orange_loc >= s:
        o_count +=1

print (a_count)
print (o_count)
