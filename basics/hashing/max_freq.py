a=[10,5,10,15,3,5,1,6,4,5]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
m=-1
x=None
for i in d:
    if m<d[i]:
        m=d[i]
        x=i
print('key is:',x,'freq :',m)
