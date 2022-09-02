a=[9, -3, 3, -1, 6, -5]
s=0
m=0
d={}
for i in range(len(a)):
    s+=a[i]
    if s==0:
        m=i+1
        print(m)
    else:
        if s in d:
            m=max(m,i-d[s])
        else:
            d[s]=i
    print(m,d,s,i)

print(m)
