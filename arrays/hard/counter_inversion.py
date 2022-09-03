def merge(a,t,l,m,r):
    ic=0
    i=l
    j=m
    k=l
    while i<=m-1 and j<=r:
        if a[i]<=a[j]:
            t[k]=a[i]
            k+=1
            i+=1
        else:
            t[k]=a[j]
            k+=1
            j+=1
            ic=ic+(m-i)
    while i<=m-1:
        t[k]=a[i]
        k+=1
        i+=1
    while j<=r:
        t[k]=a[j]
        k+=1
        j+=1
    for i in range(l,r+1):
        a[i]=t[i]
    return ic
def merge_sort(a,t,l,r):
    ic=0
    if r>l:
        m=(r+l)//2
        ic+=merge_sort(a,t,l,m)
        ic+=merge_sort(a,t,m+1,r)
        ic+=merge(a,t,l,m+1,r)
    return ic
a=[5,3,2,1,4]
t=[0]*len(a)
print(merge_sort(a,t,0,len(a)-1))
