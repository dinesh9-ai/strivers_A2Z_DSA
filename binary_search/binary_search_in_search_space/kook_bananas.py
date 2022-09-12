piles=[3,6,7,11]
h=8
import math
l,hi=1,max(piles)
while l<hi:
    m=l+(hi-l)//2
    print(l,hi,m)
    hr=0
    
    for i in piles:
        hr+=math.ceil(i/m)
    if hr>h:
        l=m+1
    else:
        hi=m
print(l)
