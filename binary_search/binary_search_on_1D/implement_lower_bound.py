a=[1,2,8,10,11,12,19]
k=5
l,e,r=0,len(a),-1
f=False
while l<e:
    m=l+(e-l)//2
    if a[m]==k:
        print(a[m])
        f=True
        break
    elif a[m]>k:
        e=m-1
    else:
        r=a[m]
        l=m+1
if not f:
    print(r)
