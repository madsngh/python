#_*_coding: utf=8_*_
'''this prog is for loops'''
a=input("please entre a sentence \n")
# for seperating elemnts in a string
def break_word(sen):
 word=sen.split(' ')
 printvalue(word)
def printvalue(a):
 for i in a:
  print("the string entered were %s"%i)
break_word(a)
#for printing star pattern
for k in range(0,6):
 for b in range(0,k):
  print("*",end="")
 print()
#for appennding elements in a list
elements=[]
asci2=[]
for i in range(65,69):
 a=chr(i)
 m=ord(a)
 elements.append(a)
 asci2.append(m)
del elements[1] 
for i in elements:
 print("%s"%i) 
for i in asci2: 
 print("%s"%i)