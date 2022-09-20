s="(1+(2*3)+((8)/4))+1"

def maxdep(s):
    a=0
    c=0
    for i in s:
        if i=='(':
            c+=1
            a=max(a,c)
        elif i==')':
            c-=1
    return a

print(maxdep(s))
