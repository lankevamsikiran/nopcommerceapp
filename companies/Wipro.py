
# a=[]
# b=[]
#
# if a is b:
#     print("True")
# else:
#     print("False")
#
# x=lambda a,b:a+b
# print(x(1,3))


#Name ,age
#10 rec
# import openpyxl
#
# workbook=openpyxl.load_workbook()
# sheet=workbook.active
#
# rows=sheet.max_row
# column=sheet.max_column
#
# for i in range(1,row+1):
#     if sheet.cell(i,1).value =="vamsi":
#         print(sheet.cell(i,2).value)
#
#
#
#
# st="Hyderabad is beautifully city capital of telanagana"
#
# l=st.split(" ")
#
# string=sorted(l, key=len)
#
# print(string[-1])
#
#
#
# a=[]
# b=[]
# print(id(a))
# print(id(b))
# if a == b:
#     print("True")
#



#print(1,2,3)

"""Write a function that takes a list as its parameter and
->returns
the
maximum
number if the
list
has
only
integers or floats
->returns
the
message
" the list does not contain numeric"

[1, 2, 3][1, 3.14, 2.3][1, 2, "abc"]

"""
#
# def max_num(A):
#
#     try:
#         return max(i for i in A)
#     except TypeError:
#         return  TypeError("Could not find digits")
#
#
# A=[1, 2,"abc"]
#
# print(max_num(A))



# def fun1(b,a=5):
#     print(a+b)



#Write a function that takes a list and dictionary
#as inputs and replaces the keys of the dictionaries with list values.

#[1,2,3] {'w1':'hi','w2':'hello','w3':'bye'}

#
# def fun(A,B):
#     #
#     # for i in A:
#     #     for j in B.values():
#     #         D[i]=j
#     # return D
#
#     dict={ x:y for x,y in zip(A,B.values())}
#     return dict
#
# A=[1,2,3]
# B={'w1':'hi','w2':'hello','w3':'bye'}
#
# print(fun(A,B))
#

"""
{'m1': ({'p1': {'f1': 'v1','f2':'v2'}},{'p2': {'p21': ['111','222'],
                                                  'p22': ['234','456']}}),
'm2': ({'p1': {'f1': 'v1','f2':'v2'}},{'p2': {'p21': ['222','333'],
                                                  'p22': ['789','012']}})}

"""
#
# dict={'m1': ({'p1': {'f1': 'v1','f2':'v2'}},{'p2': {'p21': ['111','222'],
#                                                   'p22': ['234','456']}}),
# 'm2': ({'p1': {'f1': 'v1','f2':'v2'}},{'p2': {'p21': ['222','333'],
#                                                   'p22': ['789','012']}})}
#
#
#
# for key,value in dict.items():
#     #print(value)
#     for a in value:
#         #print(a)
#
#         for i,j in a.items():
#             #print(i,j)
#             for x,y in j.items():
#                 print(y)
#
#
#
#
