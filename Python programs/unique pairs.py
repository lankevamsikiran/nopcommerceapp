

li=[["U1","U2"],["U3","U4"],["U1","U5"],["U2","U1"],["U3","U4"]]

from collections import Counter
ctr = Counter(frozenset(x) for x in li)

unique_list=[]
for i in list(ctr):
    unique_list.append(list(i))

print(unique_list)

