a=[1,4,8,10]
b=[1,3,9]
n,m=len(a),len(b)

def gap(g):
    if g<=1:
        return 0
    return g%2+g//2
g=gap(n+m)
while g>0:
    i=0
    while i+g<n:
        if a[i]>a[i+g]:
            a[i],a[i+g]=a[i+g],a[i]
        i+=1
    j=g-n if g>n else 0
    while i<n and j<m:
        if a[i]>b[j]:
           a[i],b[j]=b[j],a[i]
        i+=1
        j+=1
    if j<m:
        while j+g<m:
            if b[j]>b[j+g]:
                b[j],b[j+g]=b[j+g],b[j]
            j+=1
    g=gap(g) 
print(a,b)
