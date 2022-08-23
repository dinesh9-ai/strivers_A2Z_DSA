def Ntoone(n):
    if n<=0:
        return
    print(n)
    Ntoone(n-1)
Ntoone(9)
