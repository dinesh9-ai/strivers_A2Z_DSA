a=[7,1,5,3,6,4]
mp=0
n=len(a)
mi=10000000
for i in a:
    mi=min(mi,i)
    mp=max(mp,i-mi)
    print(mi,mp)
print(mp)
