
from collections import Counter

st="abcabcbac adgzxv sdzvx srfzbc "

a=["vamsi", "kiran","vamsi"]
b={"vamsi", "kiran","vamsi"}
c=("vamsi", "kiran","vamsi")
d= {'a': 4, 'b': 4, 'c': 4, ' ': 4, 'z': 3, 'd': 2, 'x': 2, 'v': 2, 's': 2, 'g': 1, 'r': 1, 'f': 1}

print(Counter(st))
print(Counter(a))
print(Counter(b))
print(Counter(c))
print(Counter(d))

#NOTE :
"""
COUNTER will give output as a dictionary.
we can use SET also but it will give value as 1 for all keys.
we can use dictionary also but it will give the same as output"""

