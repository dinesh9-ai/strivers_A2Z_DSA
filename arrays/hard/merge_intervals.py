a=[[1,3],[2,4],[2,6],[8,9],[9,11],[15,18],[16,17]]
a.sort(key=lambda x:x[0])
m=[]
for i in range(len(a)):
    if m==[] or m[-1][1]<a[i][0]:
        m.append([a[i][0],a[i][1]])
    else:
        m[-1][1]=max(m[-1][1],a[i][1])
print(m)
