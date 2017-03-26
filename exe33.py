'''this is while'''
'''this is while'''
n=int(input("please entre a integer\n"))
s=0
while(n>0):
 r=n%10
 s=r+s
 n=n//10
print("the value of sumation is %r"%s)