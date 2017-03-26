class Siddharth:
    name=None
    height=None
    weight=None
    age=None
    def __init__(self,name,height,weight,age):
        self.name=name
        self.height=height
        self.weight=weight
        self.age=age
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def toString(self):
        return "{} abcd {} %.5f".format(self.name,self.age)%self.weight
Human = Siddharth("Siddharth",200,64,20)
print(Human.getName())
print(Human.toString())