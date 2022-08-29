a=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,0,0,1]]
c=True
for i in range(len(a)):
    if a[i][0]==0:
        c=False
    for j in range(1,len(a[0])):
        if a[i][j]==0:
            a[i][0]=0
            a[0][j]=0
for i in range(len(a)-1,-1,-1):
    for j in range(len(a[0])-1,-1,-1):
        if a[i][0]==0 or a[0][j]==0:
            a[i][j]=0
    if c==0:
        a[i][0]=0
print(a)
    
