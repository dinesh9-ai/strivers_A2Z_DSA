n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if j<=n-(i-1) or j>=n+(i):
            print('*',end='')
        else:
            print(end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if j<=i or j>=2*n-i+1:
            print('*',end='')
        else:
            print(end=' ')
    print()

"""

5
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""
