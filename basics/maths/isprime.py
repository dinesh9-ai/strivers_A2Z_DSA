n=int(input())
x=int(n**(1/2))
f=0
for i in range(2,x+1):
    if n%i==0:
        f=1
        print('not prime')
if not f:
    print('prime')
