n=int(input())
c,o=n,n
z=[]
def gen(z,o,c):
    #print(z)
    if c==0 and o==0:
        print(*z)
        return
    if o>0:
        z.append('(')
        gen(z,o-1,c)
        z.pop()
    if c>0 and o<c:
        z.append(')')
        gen(z,o,c-1)
        z.pop()

gen(z,c,o)
