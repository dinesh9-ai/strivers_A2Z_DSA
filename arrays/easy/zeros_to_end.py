a=[1,0,2,3,0,4,0,1]
i,j=0,1
while j<len(a):
    if a[i]==0:
        if a[j]==0:
            j+=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j+=1
    else:
        i+=1
        j+=1
"""
STRIVERS Solution
n=len(a)
k=0
while k<n:
    if a[k]==0:
        break
    k+=1
i,j=k,k+1
while i<n and j<n:
    if a[j]!=0:
        a[i],a[j]=a[j],a[i]
        i+=1
    j+=1"""
print(a)
