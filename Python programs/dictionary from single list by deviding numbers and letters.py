
l=["1","2","a","b","c","d"]

numbers=[]
letters=[]

for i in l:
  if i.isdigit():
     numbers.append(i)
  else:
     letters .append(i)

if  len(letters)-len(numbers)!=0:
   for j in range(len(letters)-len(numbers)):
       numbers.append(None)

dict=dict(zip(letters,numbers))
print(dict)
