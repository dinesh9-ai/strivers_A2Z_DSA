#a=input()
a='.1'
def atoi(a):
    a=a.strip()
    if a=='':
        return 0
    n=0
    f=1
    if not a[0].isnumeric():
        p=a[0]
        a=a[1:]
        if p=='-':
            f=-1
        if p not in '+-':
            return n
    def func(s,n):
        if not(s and s[0].isnumeric()):
            return n
        
        p=s[0]
        s=s[1:]
        n=n*10+int(p)
        return func(s,n)
    
    
    n=func(a,n)
    n*=f
    if n<-(2**31):
        return -(2**31)
    elif n>(2**31)-1:
        return (2**31)-1
    else:
        return n
print(atoi(a))
