a=[3, 5, 4, 1, 1]

def peak(a):
    l,h=0,len(a)-1
    while l<=h:
        m=l+(h-l)//2
        if m==0:
            if a[0]>a[1]:
                return a[0]
            return a[1]
        if m==len(a)-1:
            if a[len(a)-1]>a[len(a)-2]:
                return a[n-1]
            return a[n-2]
        if a[m]>=a[m-1] and a[m]>=a[m+1]:
            return a[m]
        if a[m]<a[m-1]:
            h=m-1
        else:
            l=m+1
    return a[s]
print(peak(a))
