
import copy

l1=[1,2,3]
l2=copy.copy(l1)

l2[1]=6

print(l1)
print(l2)