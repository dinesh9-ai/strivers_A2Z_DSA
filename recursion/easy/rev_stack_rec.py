def ins(s,x):
    if len(s)==0:
        s.append(x)
    else:
        a=s.pop()
        ins(s,x)
        s.append(a)
def rev(s):
    if len(s)>0:
        x=s.pop()
        rev(s)
        ins(s,x)
s=[1,2,3,4]
rev(s)
print(s)
