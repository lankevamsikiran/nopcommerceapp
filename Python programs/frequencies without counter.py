
arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
#arr=["vamsi","kiran","vamsi"]
ar={}
#METHOD 1:
# for i in set(arr):
#     count=0
#     for j in arr:
#         if i==j:
#             count=count+1
#     ar[i]=count
#
# print(ar)

#METHOD 2:
for i in arr:
    if i in ar:
        ar[i] += 1
    else:
        ar[i]=1
print(ar)

