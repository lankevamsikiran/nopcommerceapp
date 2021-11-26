#1st Method

st="kiran"
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

