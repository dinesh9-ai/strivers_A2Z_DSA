a=int(input('enter number'))
n=int(input('enter root'))
l=1
h=a
while (h-l)>1e-6:
    m=(l+h)/2
    if m**n <a:
        l=m
    elif m**n>a:
        h=m

print(m)
