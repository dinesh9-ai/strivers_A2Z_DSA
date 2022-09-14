def canp(a,c,m):
    co=a[0]
    cc=1
    for i in range(1,len(a)):
        if a[i]-co>=m:
            cc+=1
            co=a[i]
        if cc==c:
            return True
    return False
def cows(a,c):
    a.sort()
    l=1
    h=a[-1]-a[0]
    while l<=h:
        m=(l+h)>>1
        if canp(a,c,m):
            r=m
            l=m+1
        else:
            h=m-1
    return r


a=[1,2,8,4,9]
c=3
print(cows(a,c))
