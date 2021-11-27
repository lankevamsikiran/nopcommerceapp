def solution(A):
    # write your code in Python 3.6
    profit = 0
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i]>A[j]:
                A[i],A[j]=A[j],A[i]

    x=min(A)
    y=max(A)
    Z=y-x
    l=A.index(x)+1
    m=A.index(y)+1




    return f"max profit {l} th day and {m}th day . Max profit is {Z}"

A=[5, 4, 3, 2]
print(solution(A))




