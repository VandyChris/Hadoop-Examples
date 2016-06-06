#!/usr/bin/env python   
#the above just indicates to use python to intepret this file

# ---------------------------------------------------------------
#This mapper code will input a line of text and output <word, 1>
# 
# ---------------------------------------------------------------

import sys             #a python module with system functions for this OS

# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------
for line in sys.stdin:  

#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
    line = line.strip()  # remove leading and trailing white spaces
    keys = line.split()  # split line at blanks (by default), and return a list of keys
    for key in keys:     #a for loop through the list of keys
        value = 1        
        print '%s\t%s' % (key, 1) # print 'word    1' where the delimiter is a tab
                                   # also, note that the Hadoop default is 'tab' separates key from the value

