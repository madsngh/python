#_*_coding: utf=8_*_
#reading a file
from sys import argv
script,filename=argv
txt=open(filename) #txt make file object it does not return content of file
print("here is the file name you wanted to read \n %r"%(filename))
print(txt.read())
txt.close()
