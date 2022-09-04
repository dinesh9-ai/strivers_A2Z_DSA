a=[2,3,7,10,13,14,17]
k=14
s=0
e=len(a)-1
f=False
while s<e:
    m=e-((e-s)//2)
    if a[m]>k:
        e=m-1
    elif a[m]<k:
        s=m+1
    else:
        f=True
        break
if f:
    print(m)
else:
    print(-1)
    
