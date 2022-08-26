def rowWithMax1s(arr):
    n=len(arr)
    c,m=0,0
    hj=-1
    for i in range(n):
        c=arr[i].count(1)
        if c>m:
            hj=i
            m=c
    return hj
arr=[[1,0,1],[1,1,1],[0,0,0]]
print(rowWithMax1s(arr))
