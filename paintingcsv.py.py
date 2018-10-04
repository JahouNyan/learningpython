# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:09:11 2018

@author: Jahou
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:32:14 2018

@author: Jahou
"""
#open and manipulate a csv file
newfile = open("paintings2.csv", "w")
csv = open("paintings.csv")
for line in csv:
    line = line.strip().split(",")
    painting = line[0]
    name = line[1]
    price = line[2]
#Try formatting the prices to a number with the appropriate number of zeroes
    editprice = float(price) * 1000000
    editprice = str(editprice)
    newline=(painting + " is a painting by " + name + " which was sold for: $ " + editprice)
    newfile.write(newline)
    newfile.write("\n")
csv.close()
    
#Ask for an extra footballer or painting and add that to the csv file    
newpainting = input("What is the name of the painting? ")
newname = input("Who is the artist? ")
newprice = input("How much was it sold for? ")
editprice = float(newprice) * 1000000
editprice = str(editprice)
newentry = (newpainting + " is a painting by " + newname + " which was sold for: $ " + editprice)
newfile.write(newentry)
newfile.write("\n")


newfile.close()

