a=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
k=3
p=len(a)
q=len(a[0])
l=0
f=False
if p!=0:
    h=(p*q)-1
    while l<=h:
        m=(l+(h-l)//2)
        if a[m//q][m%q]==k:
            f=True
            break
        if a[m//q][m%q]<k:
            l=m+1
        else:
            h=m-1
print(f)
