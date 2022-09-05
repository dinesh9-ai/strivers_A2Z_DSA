a=[1,2,8,10,11,12,19]
k=5
def ff(a,n,x):
    if x<a[0]:
        return -1
    l=0
    h=n-1
    r=0
    while l<=h:
        m=(l+h)//2
        if a[m]<x:
            l=m+1
            r=m
        elif a[m]>x:
            h=m-1
        else:
            return m
    return r
print(ff(a,len(a),k))
