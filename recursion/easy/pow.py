def pow(x,n):
    if n==0:
        return 1
    elif n%2:
        return x*pow(x*x,(n-1)//2)
    else:
        return pow(x*x,n//2)
print(pow(2,10))
