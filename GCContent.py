#SeqIO has great tools for reading different file types
# in this case, we care about fasta
from Bio import SeqIO

#bestSeq will hold the name of the best sequence
bestSeq = ""
#the current best GC content
currentBest = 0.0

#for each sequence in the fasta file
for record in SeqIO.parse("FASTA.fa", "fasta"):
        #running best is the GC content of the current file
        runningBest = 0.0
        #count number of G or C in the current sequence
        for nuc in record.seq:
            if nuc == "G" or nuc == "C":
                runningBest+=1.0
        #get the ratio
        runningBest = runningBest/len(record.seq)
        #check if its a larger ratio
        if runningBest > currentBest:
            currentBest = runningBest
            bestSeq = record.id

print bestSeq
#*100 because they want percentage
print currentBest*100
