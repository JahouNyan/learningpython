# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:45:52 2018

@author: Jahou
"""
#Assign variables to name
name1 = input("What is your name? ")
name2 = input("What is the name of your crush? ")
name1 = name1.lower().strip()
name2 = name2.lower().strip()

#reassign name variables
name1length = len(name1)
name2length = len(name2)

#convert to int
name1length = int(name1length)
name2length = int(name2length)

#preamble
print (name1 + ", your love connection to " + name2 + " is... ")

#Do some comparisons for love connection
if name1length == name2length:
    print("the definition of perfection")
elif name1length <= name2length:
    print ("hopeful")
else:
    print ("unfortunately, miles apart")
    
#Compatibilty preamble
print (name1 + ", you and " + name2 + " are: ")
    
#Character overlaps for compatability
overlap = set(name1).intersection(set(name2))
if any(overlap):
    print("Two peas in a pod")
else:
    print("You will have to agree to always disagree")
    

#Calculate similarity percentage
namelength = (name2length - name1length) 
sim = (namelength/name1length)* 100
sim = str(sim)
print(name2 + " has a " + sim + "% chance of falling in love with " + name1)