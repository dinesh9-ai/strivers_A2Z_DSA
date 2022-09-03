a=[1,3,2,3,1]
def merge(a,l,m,r):
    tot=0
    j=m+1
    for i in range(l,m+1):
        while j<=r and a[i]>2*a[j]:
            j+=1
        tot=tot+(j-(m+1))
    t=[]
    i,j=l,m+1
    while i<=m and j<=r:
        if a[i]<a[j]:
            t.append(a[i])
            i+=1
        else:
            t.append(a[j])
            j+=1
    while i<=m:
        t.append(a[i])
        i+=1
    while j<=r:
        t.append(a[j])
        j+=1
    for g in range(l,r+1):
        a[g]=t[g-l]
    return tot
def mergesort(a,l,h):
    if l>=h:
        return 0
    m=(l+h)//2
    inv=mergesort(a,l,m)
    inv+=mergesort(a,m+1,h)
    inv+=merge(a,l,m,h)
    return inv
print(mergesort(a,0,len(a)-1))

