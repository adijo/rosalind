import itertools
G = {}
input = raw_input().split(" ")

for x in range(len(input)):
    G[input[x]] = x + 1

n = int(raw_input())


def array_to_string(list):
    string = ""
    for element in list:
        string += element
    return string

def order(s1,s2):
    for x in range(len(s1)):
        if G[s1[x]] < G[s2[x]]:
            return False
        if G[s2[x]] < G[s1[x]]:
            return True
    return False


def sort(list):
    
    done = 0
    while(done!=1):
        smaug = 0
        for x in range(len(list)-1):
            if order(list[x],list[x+1]):
                temp = list[x+1]
                list[x+1] = list[x]
                list[x] = temp
                smaug = 1
                
        if smaug == 0:
            done = 1
    return list

str = ""
for element in input:
    str += element
set = []
for x in itertools.product(*[str]*n):
    set += [array_to_string(x)]
    
final = sort(set)

for element in final:
    print element
        

