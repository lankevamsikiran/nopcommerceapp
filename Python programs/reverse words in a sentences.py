str=" Hi this is vamsi"


l=str.split(" ")
li=[i[::-1] for i in l]

new_str=" ".join(li)

print(new_str)
