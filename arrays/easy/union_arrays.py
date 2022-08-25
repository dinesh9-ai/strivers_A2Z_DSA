a=[1,2,3,4,5]
b=[2,3,4,4,5]
c=[]
i,j=0,0
while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        if len(c)==0 or c[-1]!=a[i]:
            c.append(a[i])
        i+=1
    elif a[i]>b[j]:
        if len(c)==0 or  c[-1]!=b[j]:
            c.append(b[j])
        j+=1
    else:
        if len(c)==0 or c[-1]!=a[i]:
            c.append(a[i])
        i+=1
        j+=1
print(c)
