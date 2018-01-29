
#Sample data provided by Rosalind
data = "AGAACTCTTCTTCAGTAGTTCGTTCACGACTATACCGGGTACATGATTCGTCTGTTTCATGGGAAGTCAGCGATGGCATAACCTACGTTAGGAATAGAGAGCCTTGTCAATGATCGAAATTAGACTTCATCCGTTGAAGGTCGCCCACACTAGTAGCAGCTGTTACCACTAGTGAGGGAACCAGAAGAACATCGATGAAGTCCTTGGTAAGGAGTACACTTAAGTACTCGTCTCTTAGCGTGCTTGCTGAGGATCATGCCCAATAACCAGTGACCCGGCGCGCGTAGTTGATTGATCTTGATATGCGCCCTCCAGGAAGGGTGTTAATCAATGGGCCGAAAATACGACTACTGTCAGGTTTTTGACTAGTGATTAAGGCCTGCCCTGCTGGTCGCACTATGGTGTACACCGGTAGAACAGATAGCGATACCCAGTTAACATTTCTATCCCTCTGTCTGAAACGCCCGCACGCGTTGATGCTTTCCGTGCTCCACGTCGGCCCGACAGCGGCTTTGGGAGTAAGTCAAATATATGCAGTTCTCAGTTTTACCCCTCCGCAACTTACTGACAACGATCCCGTATGCTTATTGTACTTTCGGCCTATCTGTCCGTCGCCCTGTATATGTTCATGATAGCAGATACGTGCCGCCCCCAGCTACGCTCCCATGAAAGAACTCACAGTGCGCTATCAGATTCCGCACCAATCCGAATCTAGTCGTCGCTTTCAGTGCGTAGGATAAGGCCAGTGGCCGGGTGCCATGGAAGTAATTGGTCTGGTACTGCACTAATCTACGGAGCTATTCCAGGTACCGGGCACAATCGTTGCTACAGCAGAAAGAGATGCCCGTGGGTAGGCTGTAAC"
#reverse the string of data
data = data[::-1]
RNA = ""

#complement each nucleotide
for nuc in data:
    if nuc == "A":
        RNA += "T"
    elif nuc == "C":
        RNA += "G"
    elif nuc == "G":
        RNA += "C"
    elif nuc == "T":
        RNA += "A"

#print Properly
print RNA