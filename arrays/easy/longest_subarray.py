a=[7,1,6,0,0]
k=7
s,e,su,ml=0,-1,0,0
n=len(a)
while s<len(a):
    while (e+1<n) and (su+a[e+1]<=k):
        su+=a[e+1]
        e+=1
    if su==k:
        ml=max(ml,e-s+1)
    su-=a[s]
    s+=1
print(ml)
