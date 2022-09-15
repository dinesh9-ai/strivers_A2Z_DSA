a="badc"
b="baba"
def isp(a,b):
    if len(a)!=len(b):
        return 0
    d1={}
    d2={}
    for i,j in zip(a,b):
        if i in d1:
            if d1[i]!=j:
                return 0
        else:
            if j in d2:
                return 0
            else:
                d1[i]=j
                d2[j]=1
    return 1

print(isp(a,b))
