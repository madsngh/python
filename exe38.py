'''
doing things 
with list
'''
a=input("please entre a sentence \n >>")
b=["jack","king","lion","mango","out","picnic"]
c=a.split(' ')
while(len(c)!=10):
 k=b.pop()
 c.append(k)
print(c)
print(c.pop(0))