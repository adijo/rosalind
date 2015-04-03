import itertools



def make_set(data):
    set = []
    for x in range(data):
        set+=[x+1]
    return set

set = make_set(7)
ret = list(itertools.permutations(set))

print len(ret)

for element in ret:
    for single in element:
        print str(single) + " ",
    print "\n"



        
