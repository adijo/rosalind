#Aditya Joshi
#Complementing a Strand of DNA 1.0
#Rosalind


def reverse_complement(dna):
    new_dna = ""
    rev = dna[::-1]
    for element in rev:
        if element == "A":
            new_dna = new_dna + "T"
        if element == "T":
            new_dna = new_dna + "A"
        if element == "C":
            new_dna = new_dna + "G"
        if element == "G":
            new_dna = new_dna + "C"
    return new_dna




string = """CAACAGTTCGAATCTTAAAACTCTCACAGCAAGGGAATTCAATCCTTGCATTTGGGAGAGTCAGTGAGGCGATCCGTAGGAACGTAAACAGTTCACTCGCCTTGTGTTCAAAAGCCTGTAGCTATTAAAATACGCTTACGATAGCGAGCTTTCTTTTGACGGTGCAACACACAGGTCGCGGGCCTTCATCCGGGATAAATCCAATTTAAACTCGGACGCGATTGGTATATGAAGGTCCGCCCTTCGGGCGTTCATGGACCACATTATTCATAGCCCCTTCCTGGATTGCTTTTTCTTGTCAACATTGCGCTTGTCAATTACGAGGATGTCCGAGAGATGACGTACGAAGCGAAAACTCATTTGTCCTGAGTACAAAACCCTGAAACCCACTCGCCGGCGTTGACTCTAAACTGCTAAATGGCCTCTTAGTTTAAGACCACTGAACGGGGATCGGGAAGACAGAGGGCAACGTCAAGGTTAGAAATAGTTGCTTCTGGACCAGACTTGAGGTCAGCAACGTTCGGGGTCTGTAGGGCCAGTGAGGCCGACCAGCATTGCGGTGCCGCAGCCCATCGACCGCATCATCTACAGCTACATTTGTATGTGAGTCCTTGAATGCCATCTCAAATAGGTATTCCGGACTATCAGGACTTCCGCCTACGCGGATTTTTAAGGGATGCGTATTCTGGGCCGGCGCGCAGCGGAACCTATACCCATCAAGCGGACTCGTGGGCTAAAGCAGACGTTATCTGACGACACCAAGGCCCCTGTCATATCTGCTTCGAACGCGGTTGAGTGTTCTCCCTGCGCCTCTACCTTCAAGTTGAGGCCCCAGGGGGGGCCCCTATACCCCACCCCG
"""

print reverse_complement("GCATGC")
