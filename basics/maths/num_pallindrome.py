n=int(input())
x=n
r=0
while n:
    r=r*10+n%10
    n=n//10
if x==r: print('Palindrome')
else: print('not a palindrome')
