a=[8,2,1,0,3]
for i in range(len(a)-1):
    m=i
    for j in range(i+1,len(a)):
        if a[j]<a[m]:
            m=j
    if m!=i:
        a[i],a[m]=a[m],a[i]
print(*a)
