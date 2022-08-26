a=[3,2,4,6]
d={}
k=6
for i in range(len(a)):
    if (k-a[i]) not in d:
        d[a[i]]=i
    else:
        print(d[k-a[i]],i)
        break
