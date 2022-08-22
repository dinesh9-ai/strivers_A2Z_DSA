n=int(input())
for i in range(1,n+1):
    if i%2==0:
        q=0
    else:q=1
    for j in range(1,i+1):
        print(q,end='')
        if q==1: q=0
        else: q=1
    print()

"""
5
1
01
101
0101
10101
"""
