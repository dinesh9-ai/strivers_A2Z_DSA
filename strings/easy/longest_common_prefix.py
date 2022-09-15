a=["ab", "a"]
m=len(a[0])
for i in a:
    m=min(m,len(i))
i=0
q=0
while i<m:
    c=a[0][i]
    for j in a:
        if j[i]!=c:
            q=1
            break
    if q:
        break
    i+=1
print(a[0][:i])
