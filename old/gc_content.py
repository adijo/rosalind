import re

def breaker(string):
    regex = r"\>[^>]*"
    list = re.findall(regex,string)
    new_list = []
    for struct in list:
        new = re.sub("\\n"," ",struct)
        new_list += [new]
    gc_perc = {}
    for element in new_list:
        
        fasta = "Rosalind\_[0-9][0-9][0-9][0-9]"
        f_list = re.findall(fasta,element)
        code = f_list[0]
        
        dna = r"[ACGT ]+"
        d_list = re.findall(dna,element)
        dna_code = d_list[0]
        gc_perc[code] = gc(dna_code)
    return gc_perc
    



def gc(string):
    counter = 0
    total = 0
    for element in string:
        if element == "G" or element == "C":
            counter += 1
        if element != " ":
            total += 1        
    return (float(counter)/float(total)*100)



    

print breaker(""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""")
