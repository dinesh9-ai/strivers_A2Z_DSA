def sort(x,s):
    if len(s)==0 or s[-1]<x:
        s.append(x)
    else:
        a=s.pop()
        sort(x,s)
        s.append(a)
def rev(s):
    if len(s)>0:
        x=s.pop()
        rev(s)
        sort(x,s)

s=[2,5,3,1]
rev(s)

print(s)
