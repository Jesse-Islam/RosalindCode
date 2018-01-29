s = "CGGCATGTAGATAGCATGTAACATGCATGTATTGCATGTAAAGAGAGGCATGTAAGCATGTAAGCATGTAAGTCTGCATGTATCGCATGTAAGGCATGTATGCATGTAGGGCATGTACCTGCGCATGTAACCTTAGCATGTAAGGAGCATGTAAAGCTTGCTTGTCGCATGTACGCATGTAGCATGTATTTGCATGTACAGCATGTAGCATGTAGCATGTATTGAGCATGTATCGGGGCATGTAAGCGGCATGTATTGGAGCATGTATAGCGGCATGTAGCATGTAGCATGTAAGCATGTATTTGCATGTAGCATGTACGCATGTAAGGATAGGCATGTAGCATGTATGCATGTACAATGGGCATGTAGGGCATGTAAAGGAGCATGTAGGCATGTATAATGCATGTAGCATGTAGTGCATGTAGACGGCATGTAACCGCTCTGCGCATGTACATGCATGTACTAGCATGTAATGGTGCATGTAGTATGCATGTAATATCCACGATACCGCATGTAATCGCATGTAAGCATGTAGCGGCATGTAAGCATGTAGGGGCATGTAGGCATGTAGCATGTACGAGAGCATGTAGCATGTAGGCATGTATGGTAGCATGTAGTCGGACTGCATGTACTTTGGCATGTAGCATGTACTACGGCATGTAGCATGTATTCGCATGTAGCATGTAGCATGTAAACCTGGAGCATGTAGCATGTATAGGCATGTAGCATGTAGCATGTAAAGAACTTGGCCACCTTGCATGTAGAGCATGTACCTGCGAGGCATGTAGCATGTAGGGCATGTAGCATGTACAGCATGTACGCATGTAGCATGTA"
t= "GCATGTAGC"

#answer will store the final answer
ans = ''
#for every possible start point (which length of s - length of t)
for i in range (len(s)-len(t)):
    count = 0
    #compare the sequence of length t to length s. if they all match, store
    #position.
    for j in range (len(t)):
        if s[i+j] == t[j]:
            count += 1
    if count == len(t):
        ans += str(i+1)
        ans += " "
print ans
