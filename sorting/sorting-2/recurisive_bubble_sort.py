a=[8,3,9,2,0,1]
def bs(a,n):
    if n==1:
        return
    c=0
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            c+=1
    if c==0:
        return
    bs(a,n-1)

bs(a,len(a)-1)
print(a)
