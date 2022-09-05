def getFloorAndCeil(a, n, k):
    # code here
    x,y=1000000,-1000000
    for i in a:
        if i>=k and i<x:
            x=i
        if i<=k and i>y:
            y=i
    if x==1000000 and y!=-1000000:
        return (y,-1)
    elif x!=1000000 and y==-1000000:
        return (-1,x)
    elif x==1000000 and y==-1000000:
        return (-1,-1)
    return (y,x)
