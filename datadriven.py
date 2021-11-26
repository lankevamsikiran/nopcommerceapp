import XLutils



path="F:/pycharm practice/nopcommerceApp/database/Book1.xlsx"

print(XLutils.numrows(path,"vamsi"))

print(XLutils.nuumcol(path,"vamsi"))


print(XLutils.getdata(path,"vamsi",2,2))

print(XLutils.editdata(path,"vamsi",2,2, "WORLD"))
print(XLutils.getdata(path,"vamsi",2,2))