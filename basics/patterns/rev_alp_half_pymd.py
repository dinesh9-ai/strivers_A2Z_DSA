n=int(input())
q=n
for i in range(n):
    f=q
    for j in range(i+1):
        print(chr(64+f),end='')
        f+=1
    print()
    q-=1

"""
5
E
DE
CDE
BCDE
ABCDE
"""
