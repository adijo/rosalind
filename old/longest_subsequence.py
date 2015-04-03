import re

regex = r"\>Rosalind\_[0-9][^ >]*"


big = """>Rosalind_1
GATTACTACA
>Rosalind_2
TAGACCTACA
>Rosalind_3
ATACATAC
>Rosalind_3
ATTACACA
>Rosalind_3
ATTACACA
>Rosalind_3
TACATACA
>Rosalind_3
ATACTACATAC
>Rosalind_3
ATACATAC
>Rosalind_3
ATACATAC
>Rosalind_3
ATACTACA
>Rosalind_3
ATACA"""
array = re.findall(regex,big)

common = []

olongo = r"[GCAT]+"
for element in array:
    find = re.findall(olongo,element)
    common+=[find[0]]



def shortest(list):
    consider = 0
    min = list[0]
    for x in range(len(list)):
        if len(list[x]) < len(min):
            min = list[x]
            consider = x
    return list[consider]

def longest(list):
    max = list[0]
    consider = 0
    for x in range(len(list)):
        if len(list[x]) > len(max):
            max = list[x]
            consider = x
    return list[consider]

def subsonic(list):
    short = shortest(list)
    
    candidates = []
    for x in range(len(short)):
        for y in range(x,len(short)+1):
            consider = short[x:y]
         
            
            bools = []
            for element in list:
                
                if element.find(consider) !=-1:
                    bools += [True]
                else:
                    bools +=[False]
            
            if all(bools) and consider!='' and consider not in candidates:
               candidates += [consider]
                
                
    return candidates
                
            

print longest(subsonic(common))

