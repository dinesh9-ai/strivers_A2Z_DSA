def substrings(a):
    z=[]
    for i in range(len(a)):
        for j in range(i,len(a)):
            z.append(a[i:j+1])
    return z
def naive(s,k):
    c=0
    for i in substrings(s):
        if len(set(i))==k:
            c+=1
    return c


def optimal(s,k):
    n=len(s)
    r=0
    for i in range(n):
        d=[0]*27
        dc=0
        for j in range(i,n):
            if d[ord(s[j])-97]==0:
                dc+=1
            d[ord(s[j])-97]+=1
            if dc==k:
                r+=1
            if dc>k:
                break
    return r

print(optimal('aba',2))
