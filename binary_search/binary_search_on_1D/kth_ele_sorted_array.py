a=[2,3,6,7,9]
b=[1,4,8,10]
k=5
def kt(a,b,k):
    if len(a)>len(b):
        a,b=b,a
    l=min(0,k-len(a))
    h=max(k,len(b))
    while l<=h:
        c1=(l+h)//2
        c2=k-c1
        if c1==0:
            l1=-10000
        else:
            l1=a[c1-1]
        
        if c2==0:
            l2=-10000
        else:
            l2=b[c2-1]
        if c1==len(b):
            r1=10000
        else:
            r1=a[c1]
        if c2==len(a):
            r2=10000
        else:
            r2=b[c2]

        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            h=c1-1
        else:
            l=c1+1
    return 1

print(kt(a,b,k)) 
