#_*_coding: utf=8_*_
'''in this exercize we will copy a file from one file to another'''
from sys import argv
from os.path import exists
script,sour,tar=argv
print("enter CTRL C to abord")
print("hit return to continue")
input("?")
print("does source exists %r",exists(sour))
print("does targt exists %r",exists(tar))
source=open(sour,'r')
target=open(tar,'w')
sourcedata=source.read()
print("input file is %r bytes long"%(len(sourcedata)))
target.write(sourcedata)
print("closing files")
source.seek
source.close()
target.close()
#exists return type is boolean