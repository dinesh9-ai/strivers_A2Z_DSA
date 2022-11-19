s=input()
f=[]

def gen(i,s,f):
    if i==len(s):
        print(*f)
        return
    f.append(s[i])
    gen(i+1,s,f)
    f.pop()
    gen(i+1,s,f)

gen(0,s,f)
    
"""
Bit Manipulation
"""

def genn(s,n):
    for i in range((2**n)-1):
        p=''
        for j in range(0,n-1):
            if (i&(1<<j)):
                p+=s
        print(p)
