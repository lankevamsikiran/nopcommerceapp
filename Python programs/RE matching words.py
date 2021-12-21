import re

Str = "sat, hat, mat, pat, jat"

someStr = re.findall("[h-m]at", Str)

for i in someStr:
    print(i)