a=[ 4,2,2,6,4]
d={}
b=6
cpx=0
c=0
for i in range(len(a)):
    cpx=cpx^a[i]
    if cpx==b:
        c+=1
    h=cpx^b
    if cpx in d:
        c=c+h
    d[cpx]=d.get(cpx,0)+1
    print(i,cpx,c,h,d)
print(c)
