#!/usr/bin/env python

# Import needed libraries
import os
import sys

# Make sure there is one argument after the executable - this is the
# name of the file we want to open
# The script name is always the first argument. The second argument
# will be the name of the file
if len(sys.argv) != 2:
  print "Please enter the name of the file to be read after the python file"
  sys.exit()

# Using 'with' is the best way to open files in Python
with open(sys.argv[1], 'r') as f:
  # This is not always a good idea for big files. This stores all the lines
  # into memory.
  lines = f.readlines()

  # If the first line is a comment line, remove the next hash symbol
  #lines.pop(0)

# The file automatically closes when we leave the with statement

# This is a list
row = []

# Implement a counter
counter = 0

# Open up the output file for writing
with open(sys.argv[1] + '.out', 'w') as f:
  # Loop through every line in the input file
  for line in lines:
    counter += 1

    # The split function splits a line by spaces by default and returns
    # a list of space-delimited items. 'extend()' is used to add a list
    # onto another list
    row.extend(line.split())

    # Every 6 lines, create a new row and add at to the output file
    # If we are on line 6, write this to the file and keep going
    if counter == 6:
      # Loop through all the elements of the list and write them in the file
      for item in row:
        f.write(item + " ")
      # Write the return
      f.write("\n")
      # Now clear the list and start over
      row = []
      counter = 0

