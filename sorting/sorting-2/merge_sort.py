a=[8,3,1,0,2]
def merge(a):
    if len(a)==1:
        return a
    a1=a[:(len(a))//2]
    a2=a[(len(a))//2:]
    a1=merge(a1)
    a2=merge(a2)
    return mergesort(a1,a2)
def mergesort(a,b):
    c=[]
    while len(a) and len(b):
        if a[0]<b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    while len(a):
        c.append(a[0])
        a.pop(0)
    while len(b):
        c.append(b[0])
        b.pop(0)
    return c
c=merge(a)
print(c)
