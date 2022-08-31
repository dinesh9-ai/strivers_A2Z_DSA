n=5
a=[]
for i in range(1,n+1):
    z=[]
    c=1
    for j in range(1,i+1):
        z.append(c)
        #print(c*((i-j)//j),c*(i-j)//j,c,i,j)
        c=c*(i-j)//j
    a.append(z)
print(a)
