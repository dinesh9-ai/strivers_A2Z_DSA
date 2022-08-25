#find second maximum element without asorting

a=[1,9,-32,3,54,212,-1,-10,2,0]
m=-100000
m2=-10000000
for i in a:
    if i>m:
        m2=m
        m=i
print(m2)
