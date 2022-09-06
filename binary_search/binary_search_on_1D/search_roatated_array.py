a=[4,5,6,7,0,1,2]
t=0
def bsr(a,t):
    l,h=0,len(a)-1
    while l<=h:
        m=l+(h-l)//2
        if a[m]==t:
            return m
        if a[l]<=a[m]:
            if a[l]<=t and t<=a[m]:
                h=m-1
            else:
                l=m+1
        else:
            if a[m]<=t and t<=a[h]:
                l=m+1
            else:
                h=m-1
    return -1
print(bsr(a,2))
