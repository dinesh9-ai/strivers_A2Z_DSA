weights=[1,2,3,4,5,6,7,8,9,10]
days=5
        
l,r=0,0
for i in weights:
    l=max(l,i)
    r+=i
    
while l<r:
    m=l+(r-l)//2
    print(m,l,r)
    d=1
    c=0
    for i in weights:
        if i+c>m:
            d+=1
            c=0
        c+=i
        
    if d>days:
        l=m+1
    else:
        r=m
print(l)
