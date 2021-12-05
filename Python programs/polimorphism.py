
class one:
    def maths(self,a,b):
        print(a+b)
        print(a-b)

class two(one):
    def maths(self,a,b):
        super().maths(a,b)
        print(a*b)
        print(a/b)
class three(two):
    def maths(self,a,b):
        super().maths(a,b)
        print(a%b)


t=three()
t.maths(20,10)


