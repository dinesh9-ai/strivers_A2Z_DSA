def optimal(s):
    n=len(s)
    r=0
    for i in range(n):
        d={}
        for j in range(i,n):
            d[s[j]]=d.get(s[j],0)+1
            r+=(max(d.values())-min(d.values()))
    return r
print(optimal('aabcb'))
