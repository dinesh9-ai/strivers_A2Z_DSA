a=[1]
s=0
ms=0
for i in a:
    s+=i
    if s>ms:
        ms=s
    if s<0:
        s=0
print(ms)
