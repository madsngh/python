#_*_coding: utf=8_*_
from sys import argv
from os.path import exists
script,filename=argv
def prints(f):
 print(f.read())
def rewind(f):
 print("now i will print each line one by one")
 f.seek(0)
'''seek makes the interpretor to go to given line'''
def printonebyone(currentline,f):
 print("%r  %s"%(currentline,f.readline()))
print("now i am going to print everything") 
file=open(filename)
prints(file)
print("now i am going to print each line one by one")
rewind(file)
currentline=1
printonebyone(currentline,file)
currentline=currentline+1
printonebyone(currentline,file)
currentline=currentline+1
printonebyone(currentline,file)
file.close()