
a=[15,2,3,4,5,10,1,9,20]

second_large=0
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if a[i]>a[j]:
			a[i],a[j]=a[j],a[i]
		second_large=a[i]

print(second_large)

