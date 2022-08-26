a=[3,1,2,5,5]

"""
METHOD- I
def repNo(arr):
    n=len(arr)
    x=-1
    for i in range(n):
        if arr[abs(arr[i])-1]>0:
           arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        else:
            return abs(arr[i])
def missNo(arr):
    for i in range(len(a)):
        if arr[i]>0:
            return i+1
print(repNo(a))
print(missNo(a))
"""

def repNo(a):
    n=len(a)
    s=(n*(n+1))/2
    p=(n*(n+1)*(2*n+1))/6
    for i in a:
        s-=i
        p-=(i*i)
    m=(s+p/s)/2
    r=m-s
    return (m,r)
print(repNo(a))
#print('Repating No {} Missing No {}'.format(repNo(a)))
