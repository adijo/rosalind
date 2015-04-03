#Rosalind problem 1
#Computational Biology


def find(string):
    map = {}
    for element in string:
        if element not in map:
            map[element] = 1
        else:
            map[element] = map[element] + 1
    return map


string = """GAGGAACTTTGGAGGGGTGCATTGATCTCATGTACAAACCCACGCTCCGTCACCCGCACCTCTGCGTACCGGTCCTCTGGAAACTTGAACTCGCTAGACATTTCCCAAAGAGGATATATCTACCCTAAAAACGCGTCAGCAAGAGGTCTGCCGGTTTCTGCTTTAAAATGAAGACCTTTCAGCGAACCGGCACCCGAACGCTATCACCGTACGCTAGTTCAGCGAGTGGAACTCCCATTAAACCGAACGGGAAGATCGGTCCGGGTACGGGAGCCTGCCCGCATCTATAAATAAGTTTGCATTTATAGGACAGGGAATGACCTAGGACGAGGACATTCCAACACTATTCTACGTGCCCATCGCGGTGACGGGGCCTCGTAAGGTCCAGCGCGCCTGGATTAGAACATGCAGGAACCGGTTTGGTTGGGGTACCGTACCCACCTCTAGCGGATCGGTAATTTAGCATCAGGTTGGGACCGTGGACAGTAGTCGCACTTGGTCTCAGTCCCCTCTTTCAGTGGCTGTGTGAGTAAGTGGCCTTTTCCTTAGCAATGCAATGACATTCGCCGGCTTTATCGAGCGCGGCCAATATTAATGTATAAATGGTGGGCCCCTCAAGATCAGATCTACCGTAAGATTAGGTGTCCGAGTAGCCGACAACGCATGCGTCCAATCATAGTCGTGGATGAAGAATGACGACTGCGGCCACGTACGGGGAAGACCGACCTTACGTTAAAACCACCCCGCCAGGAGAAGTTTCACCGAAGGCGCCTAACAACTCAAGTCCGTAAAAGCTGAGGGGTCCGATACCACTGGTCCGATGGACAGACACGCCATGAGGCTATTAACTCAGTCTGGATGCTGTATTATCTCGGGCATCTCAATATATAGAAGAGGCGCGATCGCGTGCATACTTGATT
"""

print find(string)
