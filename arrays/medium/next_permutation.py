a=[2,1,3]
n=len(a)
k=n-2
while k>=0:
    if a[k]<a[k+1]:
        break
    k-=1
if k<0:
    a=a[::-1]
else:
    l=n-1
    while l>k:
        if a[l]>a[k]:
            break
        l-=1
    a[k],a[l]=a[l],a[k]
    q=a[:k+1]
    w=a[k+1:]
    a=q+w[::-1]
print(a)
