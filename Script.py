#!/usr/bin/python python
#title           :QE_view_dynamics.py
#description     :This will create a ascii file for visualizing dynamic motion from QE.
#author          :Tiange BiI and beautiful niloofar
#date            :
#version         :0.1
#usage           :python pyscript.py
#notes           :
#python_version  :2.7.5
#==============================================================================
import sys
f = open('Anime.ascii', 'w')

#get information for unit cell"
a_length = raw_input("Pleae enter cell length for a: ")
b_length = raw_input("Pleae enter cell length for b: ")
c_length = raw_input("Pleae enter cell length for c: ")
alpha_angle = raw_input("Pleae enter cell angle for alpha: ")
beta_angle = raw_input("Pleae enter cell angle for beta: ")
gamma_angle = raw_input("Pleae enter cell angle for gamma: ")
f.write("# Phonopy generated file for v_sim 3.6\n")
f.write('  '+ a_length + ' ' +  b_length + ' ' + c_length + '\n')
f.write('  ' +alpha_angle + ' ' + beta_angle + ' ' + gamma_angle + '\n')
f.write("#keyword: angdeg\n")

#get information for atomic positions"
atom_lines = raw_input('Please enter how may types of atom: ')
startline = 7 + float(atom_lines)
atom_numbers = raw_input('Please enter how may atoms: ')
endline = 8 + float(atom_numbers)

dyn_input = raw_input("Pleae enter X.dynxx input: ")
infile = open(dyn_input, "r")



atom_name = raw_input("Please type in the atom list: ")
a = atom_name.split()
for i, text in enumerate(infile):
    if i >= int(startline) and i <= int(endline):
        f.write('    ' + str(text[15:63]) + ' ' + str(a[int(i-int(startline))]) + '\n')
    else:
        pass
infile.close()
#get information for frequencies and matrices
qpt = raw_input("Please enter q point separated by ; such as '0.000000;0.000000;0.000000': ")

#to start reading from the beginning of infile
infile = open(dyn_input, "r")

count=0
for line in infile:

#  if not line.rstrip():
#    continue
   if '     freq' in line:
   
    freq = line.split()
   
    f.write("#metaData: qpt=[" + str(qpt) + ";" + freq[4]+ " \\" + '\n')

 
   
   if  line.startswith(' (') : 
    count = count +1
    force = line.split()
    f.write("#; "+force[1]+"; "+force[3]+"; "+force[5]+"; "+force[2]+"; "+force[4]+"; "+force[6]+" \\"+ '\n')
    
    
   if count%int(atom_numbers)==0 and  line.startswith(' (') : f.write("# ]"+'\n') 
     

infile.close()
f.close()
