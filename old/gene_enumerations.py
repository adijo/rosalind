#Aditya Joshi
#Enumerating Oriented Gene Ordering
from itertools import permutations,product
from math import fabs

n = int(raw_input())

def make_set(n):
    set = []
    for x in range(1,n+1):
        set += [x]
    return set


def plusAndMinusPermutations(items):
    for p in permutations(items,len(items)):
        for signs in product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]


def array_to_string(list):
    string = ""
    string += str(list[0]) + " " + str(list[1])
    return string
count = 0

for x in plusAndMinusPermutations(make_set(n)):
    print array_to_string(x)
    count += 1

print count
