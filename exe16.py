#_*_coding: utf=8_*_
from sys import argv
'''in this prog we will 
firstly delete everything in a file
then we will write it in the file'''
script,filename=argv
txt=open(filename,'w')
print("If you don't want that, hit CTRL- C (^C).")
print("If you do want that, hit RETURN.")
input()
txt.truncate()  #turncate function is used for deleting the content of a file
print("please entre three lines u want to rewritte in the file")
a=input("entre the first line")
b=input("enter the second line")
c=input("entre the third line")
print("i am going to write these lines into your file now")
txt.write(a)
txt.write("\n")
txt.write(b)
txt.write("\n")
txt.write(c)
print("closing the file")
txt.close()
