a=[[1,3,8],[2,3,4],[1,2,5]]
def csm(a,k):
    l,h=0,len(a)-1
    while l<=h:
        m=l+(h-l)//2
        if a[m]<=k:
            l=m+1
        else:
            h=m-1
    return l


def fm(a):
    l,h=1,100
    n,mi=len(a),len(a[0])
    while l<=h:
        q=h
        w=l
        m=int((l+h)//2)

        c=0
        for i in range(n):
            f=csm(a[i],m)
            c+=f
        if c<=(n*mi)//2:
            l=m+1
        else:
            h=m-1
    return l
print(fm(a))
