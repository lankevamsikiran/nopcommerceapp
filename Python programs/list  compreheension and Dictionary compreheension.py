
# TYPE 1:

mylist=[2,3,5,7,11]

squared_list=[x**2 for x in mylist]
print(squared_list)

squared_dict={x:x**2 for x in mylist}

print(squared_dict)

#TYPE 2:  CONDITIONAL FILTERING

sq_li=[x**2 for x in mylist if x%2==0]
print(sq_li)
sq_di={x:x**2 for x in mylist if x%2==0}
print(sq_di)

#TYPE 3: Combining multiple lists

a=[1,2,3]
b=[1,2,3]
c=[1,2,3]


l1=[x+y for x,y in zip(a,b)]
print(l1)

l=[x+y+z for x,y,z in zip(a,b,c)]
print(l)


#TYPE 4 :  Flattening multi dimensions:

p=[[1,2,3],[1,2,3],[1,2,3]]

p1=[s for m in p for s in m]

print(p1)