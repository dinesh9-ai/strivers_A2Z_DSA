s = "(()())(())(()(()))"
r=''
c=0
for i in s:
    if i=='(':
        c+=1
        if c>1:
            r+='('
    elif i==')':
        c-=1
        if c>0:
            r+=')'
print(r)
