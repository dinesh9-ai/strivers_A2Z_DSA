def lo(a,k):
    l,h=0,len(a)-1
    r=-1
    while l<=h:
        m=l+(h-l)//2
        if a[m]==k:
            r=m
            l=m+1
        elif a[m]<k:
            l=m+1
        else:
            h=m-1
    return r
a=[3,4,13,13,13,20,40]

print(lo(a,13))
