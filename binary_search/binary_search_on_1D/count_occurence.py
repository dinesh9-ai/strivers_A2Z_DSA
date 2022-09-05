def bs(a,k):
    l,h=0,len(a)-1
    while l<=h:
        m=l+(h-l)//2
        if a[m]==k:
            return m
        elif a[m]<k:
            l=m+1
        else:
            h=m-1
    return -1

a=[2,2,3,3,3,3,4]
x=4
i=bs(a,x)
k=1
l,r=i-1,i+1
while l>=0 and a[l]==x:
    k+=1
    l-=1
while r<len(a) and a[r]==x:
    k+=1
    r+=1
print(k)

