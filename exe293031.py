'''here we will be dealing with 
if and else if '''
#_*_coding: utf=8_*_
a=input(" please enter a word \n")
def break_words(sen):
 words=sen.split(' ')
 #word_pop(words)
def word_pop(a):
 k=a.pop(0)
 if(k=='a'):
  print("it starts with a word a")
 l=a.pop(0)
 if(l=='b'):
  print("it starts with b")
 m=a.pop(0)
 if(m=='c' or m=='d'):
  print("i feel alive")
 else:
  print("none of these")
break_words(a)