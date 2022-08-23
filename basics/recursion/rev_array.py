def rev(a,i,j):
    if i==j:
        return
    a[i],a[j]=a[j],a[i]
    rev(a,i+1,j-1)
a=[1,2,3,4,5]
rev(a,0,len(a)-1)
print(*a)
