import sys

hd=float(sys.argv[1])
ht=float(sys.argv[2])
hr=float(sys.argv[3])

total=hd+ht+hr



probr=(hr/total)*((hr-1)/(total-1)) #both recessive 
probt=(ht/total)*((ht-1)/(total-1))*0.25 #both hetero 
probrt=(hr/total)*((ht)/(total-1))*.5 #res het 
probtr=(ht/total)*((hr)/(total-1))*.5 #het res 

negp=probr+probt+probrt+probtr


print(1-negp)

