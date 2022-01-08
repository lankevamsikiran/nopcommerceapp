
arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
#arr=["vamsi","kiran","vamsi"]
ar={}

for i in set(arr):
    count=0
    for j in arr:
        if i==j:
            count=count+1
    ar[i]=count

print(ar)
