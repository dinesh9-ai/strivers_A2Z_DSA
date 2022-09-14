a=[12,34,67,90]
b=2
h=0
for i in a:
    h+=i

def isp(t,b):
    c=1
    f=0
    for i in a:
        if i+f>t:
            c+=1
            f=0
        f+=i
    return c

l=a[0]
while l<=h:
    m=(l+h)>>1
    if isp(m,b)<=b:
        h=m-1
    else:
        l=m+1

print(l)
