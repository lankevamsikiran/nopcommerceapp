#
# l=[2,3,5,7,8]
#
# sq={i:i**2 for i in l if i%2==0}
#
# print(sq)
#
#print(st)

# a=list(map(int,st))
#
# print(a)
#
# print(sum(a))

# import re
# STRING = "1abc2x30yz67-20"
#
# st=re.findall("\d+", STRING)
# print(st)
# print(sum(list(map(int,st))))
#
# import re
# STRING = "1abc2x30yz67-20"
#
#
# st=re.split("[^0-9]+",STRING)
# print(st)
#
#
# a=list(map(int,st))
# print(a)
# print(sum(a))


#STRING = "1abc2x30yz67-20"

# STRING="a5b55c555"
#
# def sumnum(STRING):
#     sum=0
#     a="0"
#     for i in STRING:
#         if i.isdigit():
#             a=a+i
#         else:
#
#             sum=sum+int(a)
#             a="0"
#     return sum+int(a)
#
# print(sumnum(STRING))

#
# queries = ["add hack","add hackerrank","find hac","find hak"]
#
# l=[]
#
# for i in queries:
#     if "add" in i:
#         a=i.split(" ")
#         l.append(a[-1])
#     elif "find" in i:
#         b=i.split(" ")
#         for j in l:
#             if b[-1] in j:
#                 print(j)
#
#
# print(l)
