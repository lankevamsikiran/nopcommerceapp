

def deco(funct):
    def low():
        a=funct()
        L=a.lower()
        return L
    return low

def spl(funct):
    def splitt():
        b=funct()
        s=b.split(" ")
        return s
    return splitt

def jon(funct):
    def jo():
        c=funct()
        j=" ".join(c)
        return j
    return jo
@jon
@spl
@deco
def changetolow():
    return "HELLO World VAMSI"

print(changetolow())

