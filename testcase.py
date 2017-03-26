import heapq
import numpy as np
word="hi"
print(word[0:2])

s=['a','b','c','d','a']
print(list(set(s)))
print(s.index('b'))
s.insert(0,"hello")
print(s)
s=[1,10,5,19]
print(heapq.heapify(s))
arr=[1,2,3,4,5]
i=0
j=2
#str(input())


#list[::-1] is used to reverse the etire list.
#-1 represent step if -2 is provided even step willl b revesed counting from end
#if 2 is provided it will print even index elemets starting from 0th index
print(arr[::-1])

h=('a','b','c','d')
print(list(h).index('a'))
if('z' not in h):
    print("i m not in tuple")



for i in range(4,-1,-1):
    print(i)





z="12345"
b=sum(list(map(int,z)))
print("sum is",b)



'''for i in range(1,1377):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
            break
    if(count==0):
        print(i)'''



l=[1,2,3,4,5,6,7,8]
l=np.square(l)
print(l)
#!/bin/python3


word ="hello how are you"
l=word.split(" ")
print(l)
for z in l:
    print(z)

