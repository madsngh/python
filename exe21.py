def add(*a):
 c,d=a
 print("the no are %r %r"%(c,d))
 return (c+d)
def sub(*a):
 c,d=a
 print("the no are %r %r"%(c,d))
 return(d-c)
def mul(*a):
 c,d=a
 print("the no are %r %r"%(c,d))
 return (c*d)
def div(*a):
 c,d=a
 print("the no are %r %r"%(c,d))
 return (d/c)
suma=add(30,5)
subs=sub(5,30)
multi=mul(30,5)
divi=div(5,30)
print("the sum is %r \n sub is %r \n mul is %r \n div is %r \n"%(suma,subs,multi,divi))
