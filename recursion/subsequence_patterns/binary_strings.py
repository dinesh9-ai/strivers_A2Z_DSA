k=int(input())
s=[0]*k

def gen(k,s,n):

    if n==k:
        print(*s)
        return 
    if s[n-1]==1:
        s[n]=0
        gen(k,s,n+1)
    else:
        s[n]=0
        gen(k,s,n+1)
        s[n]=1
        gen(k,s,n+1)


s[0]=0
gen(k,s,1)
s[1]=1
gen(k,s,1)
