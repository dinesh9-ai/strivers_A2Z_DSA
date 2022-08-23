n=int(input())
x=n
c=0
while x:
    x=x//10
    c+=1
x=n
r=0
while x:
    r=r+(x%10)**c
    x=x//10
print(r==n)
