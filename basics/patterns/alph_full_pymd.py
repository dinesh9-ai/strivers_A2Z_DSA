n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=' ')
    c=0
    for j in range(i):
        print(chr(65+c),end='')
        c+=1
    c-=1
    while c!=0:
        c-=1
        print(chr(65+c),end='')
    print()

"""
5
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

"""
