a=[4,5,6,7,0,1,2]
def mbs(a):
    mi=10000000
    l,h=0,len(a)-1
    while l<=h:
        if a[l]<a[h]:
            mi=min(mi,a[l])
            break
        m=l+(h-l)//2

        if a[l]<=a[m]:
            mi=min(mi,a[l])
            l=m+1
        else:
            mi=min(mi,a[h])
            h=m-1
    return mi
print(mbs(a))
