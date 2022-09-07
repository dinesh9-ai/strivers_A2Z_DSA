def ar(a):
    l,h=0,len(a)-1
    while l<=h:
        m=l+(h-l)//2
        if a[m]<a[m-1]:
            return m

        if a[h]>a[m]:
            h=m-1
        else:
            l=m+1

