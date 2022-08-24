a=[8,2,9,2,0,1]
def ins(a,x):
    if x==len(a):
        return
    j=x
    while j>0 and a[j]<a[j-1]:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
    ins(a,x+1)
ins(a,0)
print(a)
