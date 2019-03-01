import sys
import itertools


def overlap(s1, s2, k):
    return s1[-k:] == s2[:k]
#ref for function https://stackoverflow.com/questions/27878067/rosalind-overlap-graphs



sequences=[]



from Bio import SeqIO
for record in SeqIO.parse("rosalind_grph.txt", "fasta"):
    sequences.append([record.id,str(record.seq)])



print(sequences[1][1][-4])
k=int(sys.argv[1])
#print(sequences)
#hammed".endswith(suffix[, start[, end]])
edges = []
for u,v in itertools.combinations(sequences, 2):
    if overlap(u[1], v[1], k):
        edges.append([u[0],v[0]])
    if overlap(v[1], u[1], k):
        edges.append([v[0],u[0]])

for i in range(0,len(edges)):
    print(" ".join(edges[i]))
