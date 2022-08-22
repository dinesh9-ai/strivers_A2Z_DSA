n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(j,end='')
        else:
            print(end=' ')
    for j in range(n,0,-1):
        if j<=i:
            print(j,end='')
        else:
            print(end=' ')
    print()

"""

5
1        1
12      21
123    321
1234  4321
1234554321

"""
