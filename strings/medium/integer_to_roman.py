d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,
   'XL':40,'XC':90,'CD':400,'CM':900}

n=3
r=''
for hj in sorted(d,key=lambda x:d[x],reverse=True):
    i,j=hj,d[hj]
    if n//j:
        c=n//j
        r+=i*c
        n=n%j

print(r)
