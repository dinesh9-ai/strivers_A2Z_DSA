a=[8,1,0,3,2]
for i in range(len(a)):
    j=i
    while j>0 and a[j]<a[j-1]:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
print(*a)
