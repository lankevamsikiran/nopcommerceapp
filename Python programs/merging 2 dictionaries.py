
d1={"a":100, "b":200}
d2={"c":300, "d":400}
d3={"e":500, "f":600}

d1["z"]=700
print(d1)

#1st Method:
d1.update(d2)
print(d1)

#2nd Method
x={**d1,**d2,**d3}
print(x)



