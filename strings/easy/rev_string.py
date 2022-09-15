a="this is an amazing program"
a=a.split()
i,j=0,len(a)-1
while i<=j:
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1
    
print(' '.join(a))
