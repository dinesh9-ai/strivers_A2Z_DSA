a=[7,7,7,7,12,7,7]
m=2
k=3
l,r=1,max(a)+1
ans=max(a)+1
def ca(d,k,m):
    t,c=0,0
    for i in a:
        if i<=d:
            c+=1
            if c==k:
                c=0
                t+=1
        else:
            c=0
    return t>=m
while l<=r:
    mi=(l+r)//2
    print(mi)
    if ca(mi,k,m):
        ans=mi
        r=mi-1
    else:
        l=mi+1
if ans==max(a)+1:
    print(-1)
else:
    print(ans)
