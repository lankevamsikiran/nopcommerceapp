
import collections

# def CountFrequency( arr ):
#     return collections.Counter(arr)
#
# if __name__ == "__main__":
#     arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
#     freq = CountFrequency(arr)
#     print(freq)
#     for (key, value) in freq.items():
#         print (key, " -> ", value)
#
l=[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
x=collections.Counter(l)
print(collections.Counter(l))

for key,value in x.items():
    print(key,"->",value)

