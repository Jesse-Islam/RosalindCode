from Bio import SeqIO

a=[]
for record in SeqIO.parse("rosalind_cons.txt", "fasta"):
    a.append("%s" % (record.seq))


A=[0 for col in range(len(a[1]))]
T=[0 for col in range(len(a[1]))]
G=[0 for col in range(len(a[1]))]
C=[0 for col in range(len(a[1]))]


for i in range(0,len(a)):
    for j in range(0,len(a[1])):
        if(a[i][j]=="A"):
            A[j]=A[j]+1
        elif(a[i][j]=="T"):
            T[j]=T[j]+1
        elif(a[i][j]=="G"):
            G[j]=G[j]+1
        else:
            C[j]=C[j]+1

conned=""
for i in range(0,len(A)):
    test=[A[i],T[i],G[i],C[i]]
    spot=test.index(max(test))
    if spot==0:
        conned=conned+"A"
    elif spot==1:
        conned=conned+"T"
    elif spot==2:
        conned=conned+"G"
    else:
        conned=conned+"C"
        
print(conned)
print("A:",*A)
print("C:",*C)
print("G:",*G)
print("T:",*T)
