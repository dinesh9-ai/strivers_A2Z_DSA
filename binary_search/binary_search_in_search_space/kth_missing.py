a=[2,3,4,7,11]
k=5
l,h=0,len(a)-1
ans=0
while l<=h:
    m=(l+h)>>1
    print(l,h,m,ans)
    if (a[m]-(m+1))<k:
        ans=m+1
        l=m+1
    else:
        h=m-1
print(k+ans,ans)
