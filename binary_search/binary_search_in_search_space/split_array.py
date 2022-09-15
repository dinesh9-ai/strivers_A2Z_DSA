def isp(t,k):
    cm=0
    p=1
    for i in a:
        cm+=i
        if cm>t:
            p+=1
            if p>k:
                return 0
            cm=i
    return 1

l=0
h=0
for i in a:
    h+=i
    l=max(l,i)
if k>len(a):
    return -1
r=-1
while l<=h:
    m=(l+h)>>1
    if isp(m,k):
        h=m-1
        r=m
    else:
        l=m+1
return r
