
#1st Method

st="kiran vamsi"
rev=""

for i in st:
    rev = i+rev

print(rev)

#2nd Method:

def reve(st):
    if len(st)==0:
        return st
    else:
        return reve(st[1:])+st[0]

print(reve("kiran"))


#3rd Method


a="Python"
rea=""
l=len(a)
while l>0:
    rea=rea+a[l-1]
    l=l-1
print(rea)

#4th Method:

a="Python"
print(a[::-1])

#5th Method

a="Python1"

reverse=reversed(a)
#print(reverse)
print("".join(reverse))

