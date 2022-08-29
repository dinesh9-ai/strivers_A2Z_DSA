a=[3, 8, 5, 7, 6]
"""
a.sort()
c=1
m=0
t=a[0]
for i in a[1:]:
    if abs(t-i)==1:
        c+=1
        t=i
    else:
        t=i
        c=1
    m=max(c,m)

print(m)
"""
d={}
for i in a:
    if d.get(i,0)==0:
        d[i]=1
l=0
for i in a:
    if not d.get(i-1):
        cn=i
        cs=1
        while d.get(cn+1):
            cn+=1
            cs+=1
        l=max(l,cs)
print(l)
            
