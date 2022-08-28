a=[2,1,3,4,5,6,4]
s,e=0,-1
su=0
n=len(a)
k=10
f=[]
while s<n:
    while (e+1)<n and su+a[e+1]<=k:
        su+=a[e+1]
        e+=1
    if su==k:
        for i in range(s,e+1):
            print(a[i])
    su-=a[s]
    s+=1
