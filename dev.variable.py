## in qqlist convert X.dyn0 q points to fractional coordinate
### all we need is reciprocal axes: (cart. coord. in units 2 pi/alat) b(1), b(2) and b(3) in scf.out

import numpy as np
import os
import sys
if len(sys.argv) != 2:
  print "Please enter the name of the file to be read after the python file"
  sys.exit()
# for raw_input, it reads three float number right away then we can create L list (q-point) 
a,b,c =map(float,raw_input("Please enter q point such as 0.15  0.97 -0.18: ").split())

L=[a, b, c]
## We are going to invert input(MxN) to input.out(NxM)

with open(sys.argv[1], 'r') as f: lis = [x.split() for x in f]
with open(sys.argv[1] + '.out', 'w') as wf: 
 for x in zip(*lis):
      lis='   '.join(map(str, (x)))+'\n'
      if not lis.rstrip():continue  #helps to not have extra empty line in .out file
      wf.write(lis)

#### Now we print input.dat to one row data
count=0 ; row=[]
with open('fin', 'w') as wf:
 with open(sys.argv[1] + '.out', 'r') as f:      
  for x in f: 
      T = x.split() 
      count +=1
      row.extend(T)
      if count == 3:  #depends how many lines of data isin the loop. it ignores number of columns, put 1
       for item in row:
        wf.write(item + " ")
       wf.write("\n") # Write the return
       row = [] ; count = 0 # Now clear the list and start over
#### Now preparing correct format of input for np.linalg.solve   
d = [[] for x in xrange(0,3)] #generates empty list of lists
with open('fin') as f:
   for x in f:
    lines = x.split()
    b=np.asarray(lines,dtype=None, order=None)
# we have one big array so far [''  ''  ''... ] and we need [[0.4, 0.7, 1], [ 1, 2, 3]...] 
j=0
for i in range(0,9):
#   for j in range(0,3): it repeats  same values for list. I replaced this line with j=0 
    if len(d[j])==3: j+=1
    d[j].append(b[i])
    d[j]=map(float, d[j]) #convert str '1' to integer 1. we needed a loop since we have [[],[],[]] list of lists 

print "linear matrix equation:" , d
#example L=[0.151240634813317E+00,  -0.979430270314405E-04,  -0.181568421323526E-01]

print 'q-point:' , L
print 'q-point convert from cartesian to fractional coordinates'
print np.linalg.solve(d,L)

