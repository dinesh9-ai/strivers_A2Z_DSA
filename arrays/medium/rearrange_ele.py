a=[9, 4, -2, -1, 5, 0, -5, -3, 2]
n=len(a)
i,j=0,n-1
while i<j:
    while i<n and a[i]>0:
        i+=1
    while j>=0 and a[j]<0:
        j-=1
    if i<j:
        a[i],a[j]=a[j],a[i]
if i!=0 or i!=n:
    k=0
    while k<n and i<n:
        a[k],a[i]=a[i],a[k]
        k+=2
        i+=1
print(a)
    
