
#1st method
def fact(num):
    if num ==0 or num==1:
        return 1
    else:
        return num*fact(num-1)


a=5
print(fact(a))

#2nd method:
result=1
for i in range(1,a+1):
    result=result*i

print(result)

#3rd Method:

from functools import reduce

factvalue= reduce(lambda x,y:x*y, range(1,a+1))
print(factvalue)
