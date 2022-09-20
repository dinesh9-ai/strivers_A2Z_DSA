s='aaabbc'
d={}
for i in s:
    d[i]=d.get(i,0)+1
a=sorted(d,key=lambda x: d[x])
print(d[a[-1]]-d[a[0]])
