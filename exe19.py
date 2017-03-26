#_*_coding: utf=8_*_
def siddhu(*a): #the value or r and s is laatter stored in *a
 c,d=a
 print("the values stored in the function are %r %r"%(c,d))
siddhu(10,20) #direct value is initialized
def siddhu1(*b):
 c,d=b
 print("the values stored in the function are %r %r"%(c,d))
a=10
b=20
siddhu1(a,b) #variable is given a value and then it is initialized
def siddhu2(*e):
 c,d=e
 print("the values stored in the function are %r %r"%(c,d))
siddhu2(a+40,b+50) #mathematics with variable can be done
def siddhu3(*f):
 c,d=f
 print("the values stored in the function are %r %r"%(c,d))
siddhu3(10+40,50/10) #direct mathematics can be done