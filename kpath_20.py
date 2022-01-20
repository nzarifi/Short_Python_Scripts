import numpy as np
import sys

symm = raw_input("Number of Symmetry? ")
while True:
 try:
     symm=int(symm)
     break
 except: print "Symmetry is the integer number!!"
 sys.exit()

arr=[]
inp = open ("kpath.ini","r")
##read line into array
for line in inp.readlines():
        numbers = map(float, line.split())
        arr.append(numbers)

numPoints = 20
with open('kpath.dat', 'w') as wf:

 for i in range(0,symm):
    if i == 0: continue
    xValues = np.linspace(arr[i-1][0], arr[i][0], numPoints, endpoint=True)
    yValues = np.linspace(arr[i-1][1], arr[i][1], numPoints, endpoint=True)
    zValues = np.linspace(arr[i-1][2], arr[i][2], numPoints, endpoint=True)

    for j in range(numPoints):
      string = str('{: 16.6E}'.format(xValues[j])) + ' ' + str('{: 16.6E}'.format(yValues[j])) + ' ' + str('{: 16.6E}'.format(zValues[j])) + '\n'
#      print string,   ',' has a meaning. it removes the space
      wf.write(string)

