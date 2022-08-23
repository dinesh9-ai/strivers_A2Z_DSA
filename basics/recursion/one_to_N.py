def onetoN(i,n):
    if i>n:
        return
    print(i)
    onetoN(i+1,n)
onetoN(1,9)
