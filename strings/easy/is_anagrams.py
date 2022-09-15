a='ant'
b='tan'

def isp(a,b):
    a=sorted(a)
    b=sorted(b)
    return a==b

print(isp(a,b))
