a=[2,2,1,1,1,2,2]

c,ca=0,0
for i in a:
    if c==0:
        ca=i
    if i==ca:
        c+=1
    else:
        c-=1
print(ca)
