a=[1,2,3,4]
s=a[0]
f=0
for i in range(1,len(a)):
    if s<a[i]:
        s=a[i]
    else:
        f=1
        break
if f:
    print('not sorted')
else:
    print('sorted')
