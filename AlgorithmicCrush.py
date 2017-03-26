import sys
s=input().split(" ")
N=int(s[0])
M=int(s[1])
l=[0]*N
for j in range(0,M):
   s=input().split(" ")
   a=int(s[0])-1
   b=int(s[1])
   k=int(s[2])
   for i in range(a,b):
       l[i]=l[i]+k
print(max(l))