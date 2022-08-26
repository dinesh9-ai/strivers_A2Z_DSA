a=[1,1,1,0,1,0,0]
c,m=0,0
i=0
for i in a:
    if i==1:
        c+=1
    else:
        c=0
    m=max(c,m)
print(m)
