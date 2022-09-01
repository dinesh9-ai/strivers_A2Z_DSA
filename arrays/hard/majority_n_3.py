a=[1,2,2,3,2]
n1,n2=-1,-1
c1,c2=0,0
z=[]
for i in range(len(a)):
    if a[i]==n1:
        c1=c1+1
    elif a[i]==n2:
        c2=c2+1
    elif c1==0:
        n1=a[i]
    elif c2==0:
        n2=a[i]
    else:
        c1=c1-1
        c2=c2-1
c1,c2=0,0
for i in a:
    if i==n1:
        c1+=1
    elif n2==i:
        c2+=1
if c1>len(a)//3:
    z.append(n1)
if c2>len(a)//3:
    z.append(n2)
print(z)
