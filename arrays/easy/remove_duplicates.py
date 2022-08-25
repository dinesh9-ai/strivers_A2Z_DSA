a=[1,1,1,1,2,2,3,3,3,3]
i=0
n=len(a)
while i<n-1:
    if a[i]==a[i+1]:
        del a[i+1]
        n-=1
    else:
        i+=1
print(a)
