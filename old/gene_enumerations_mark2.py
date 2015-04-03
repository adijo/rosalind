from itertools import permutations
from math import fabs

n = int(raw_input())

def make_set(n):
    input = []
    for x in range(1,n+1):
        input += [x]
        input += [x - (x*2)]
    return input

input = make_set(n)

    
def remove(list):
	#Returns True if the list is to be deleted, False if not.
	for x in range(len(list)):
		for y in range(len(list)):
			if fabs(list[x]) == fabs(list[y]) and list[x]!=list[y]:
				return True
	return False

def array_to_string(list):
    string = ""
    for x in list:
        string += str(x) + " "
    print string[:-1]
        


final = []
for x in permutations(input,n):
    if remove(x) == False:
        final += [x]


print len(final)
for element in final:
    array_to_string(element)


