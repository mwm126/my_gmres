import random

NX = 1000
NY = 1000
NZ = 1000
ijkFixed = 1

def map(i,j,k):
  return 1 + k + NZ*(j + NY*i)

fA = open("AA.dat","w")
fb = open("bb.dat","w")

for i in range(0,NX):
  for j in range(0,NY):
    for k in range(0,NZ):
      print >> fb, random.uniform(-1.0,1.0)
      ijk = map(i,j,k)

      if ijk == ijkFixed:  # fix one point to make system determinate
        print >> fA, ijk, ijk, 1.0
      else:         # build 
        centerCoeff = -6.0

        if (i == 0):
          centerCoeff += 1.0
        else:
          print >> fA, ijk, map(i-1,j,k), 1.0

        if (j == 0):
          centerCoeff += 1.0
        else:
          print >> fA, ijk, map(i,j-1,k), 1.0
        
        if (k == 0):
          centerCoeff += 1.0
        else:
          print >> fA, ijk, map(i,j,k-1), 1.0
      
        if (i == NX-1):
          centerCoeff += 1.0
        else:
          print >> fA, ijk, map(i+1,j,k), 1.0

        if (j == NY-1):
          centerCoeff += 1.0
        else:
          print >> fA, ijk, map(i,j+1,k), 1.0
        
        if (k == NZ-1):
          centerCoeff += 1.0
        else:
          print >> fA, ijk, map(i,j,k+1), 1.0   

        print >> fA, ijk, ijk, centerCoeff

fA.close()
fb.close()



      
      