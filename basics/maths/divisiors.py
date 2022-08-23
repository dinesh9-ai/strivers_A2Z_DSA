n=int(input())
x=int(n**(1/2))
for i in range(1,x+1):
    if n%i==0:
        print(i)
        if i!=n/i: print(n//i)
