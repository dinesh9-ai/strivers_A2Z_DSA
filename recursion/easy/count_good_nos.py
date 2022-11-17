def pow(x,n):
    if n==0:
        return 1
    a=pow(x,n//2)
    a*=a
    a%=((10**9)+7)
    if n%2:
        a*=x
    a%=((10**9)+7)
    return a
def gc(n):
    o=n//2
    e=n//2 + n%2
    return (pow(5,e)*pow(4,o))%((10**9)+7)
print(gc(1))
