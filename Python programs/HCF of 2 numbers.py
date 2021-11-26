
a=100
b=200

small=a if a<b else b

for i in range(1, small+1):
    if a%i ==0 and b%i ==0:
        HCF = i

print(HCF)

#2nd method:


def hcf(a,b):
    while b>0:
        a,b=b,a%b
    return a
print(hcf(a,b))

