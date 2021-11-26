
#TYPE 1 :

def fibonacci_series(num):
    a = 0
    b = 1

    while num>a:
        yield a
        a,b=b,a+b

print(fibonacci_series(10))
for i in fibonacci_series(10):
    print(i, end=" ")

