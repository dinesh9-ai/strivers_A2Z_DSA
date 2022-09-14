a=[12,34,67,90]
b=2
h=0
l=0
for i in a:
    h+=i
    l=max(l,i)

def isp(t,b):
    c=1
    f=0
    for i in a:
        f+=i
        if f>t:
            c+=1
            if c>b:
                return 0
            f=i
    return 1

r=-1
if b>len(a):
    return -1
while l<=h:
    m=(l+h)>>1
    if isp(m,b):
        h=m-1
        r=m
    else:
        l=m+1

print(r)
