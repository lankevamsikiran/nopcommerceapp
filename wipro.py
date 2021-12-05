
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

a=[]
b=[]
print(id(a))
print(id(b))
if a == b:
    print("True")

