

class calculator:
    def __init__(self, a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multi(self):
        return self.a*self.b
    def divi(self):
        return self.a/self.b

a=int(input("enter a value:"))
b=int(input("enter b value:"))
cal=calculator(a,b)

choice=1

while choice !=0:
    print("0. Exit")
    print("1. add")
    print("2. sub")
    print("3. multiplication")
    print("4. division")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(cal.add())
    elif choice==2:
        print(cal.sub())
    elif choice==3:
        print(cal.multi())
    elif choice==4:
        print(cal.divi())
    elif choice==0:
        print("Exit")
    else:
        print("invalid choice")

print()

