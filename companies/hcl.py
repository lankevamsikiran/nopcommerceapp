
# from functools import reduce
# #l=range(1,6)
# x=int(input("vallue:"))
# print(reduce(lambda x,y:x*y, range(1,x+1)))

a="vamsivamsi"
print("".join(list(set(a))))

b=""

for i in a:
    if i in b:
        continue
    else:
        b=b+i

print(b)
