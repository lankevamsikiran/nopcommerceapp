
str1=input("enter str1:  ")
str2=input("enter str2:  ")

op1=""
op2=""
for i in str1:
    if i not in str2 and i not in op1:
        op1=op1+i
for j in str2:
    if j not in str1 and j not in op2:
        op2=op2+j

print("OP1", op1)
print("OP2", op2)
