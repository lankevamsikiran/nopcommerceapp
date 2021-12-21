
test_str=input("enter string :")
print("original : ",test_str)

result=0

vowels=["a", "e", "i", "o", "u"]

for i in range(1,len(test_str)-1):

    if test_str[i] not in vowels and test_str[i-1] in vowels or test_str[i+1] in vowels:
        result=result+1
    elif test_str[0] not in vowels and test_str[1] in vowels:
        result+=1
    elif test_str[-1] not in vowels and test_str[-2] in vowels:
        result+=1

print("result :" ,result)
