import sys

dd=float(sys.argv[1])
dh=float(sys.argv[2])
dr=float(sys.argv[3])
hh=float(sys.argv[4])
hr=float(sys.argv[5])
rr=float(sys.argv[6])

edd=2
edh=2
edr=2
ehh=0.75*2
ehr=0.5*2
err=0

print(edd*dd+edh*dh+edr*dr+ehh*hh+ehr*hr+err*rr)
