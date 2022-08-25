a=[1,2,3,4,5,6,7]

def approach1(a,k):
    k=k%len(a)
    n=len(a)
    z=[]
    for i in range(k):
        z.append(a[i])
    for i in range(n-k):
        a[i]=a[i+k]
    for i in range(n-k,n):
        a[i]=z[i-n+k]
    return a

"""
def rev(a,s,e):
    a=a[s:e:-1]+a[e:]
def approach2(a,k):
    n=len(a)
    k=k%n
    rev(a,0,n-k-1)
    rev(a,k,n-1)
    rev(a,0,n-1)
    return a
"""
print(approach1(a,2))
#print(approach2(a,2))
