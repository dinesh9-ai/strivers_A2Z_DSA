n=int(input())
for i in range(n,0,-1):
    q=0
    for j in range(n,n-i,-1):
        print(chr(65+q),end='')
        q+=1
    print()
"""
5
ABCDE
ABCD
ABC
AB
A
"""
