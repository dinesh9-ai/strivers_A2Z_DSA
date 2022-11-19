k=int(input())
s=[None]*k

def gen(k,s,n):

    if n==k:
        print(*s)
        return 
    
    s[n]=0
    gen(k,s,n+1)
    s[n]=1
    gen(k,s,n+1)


gen(k,s,0)
