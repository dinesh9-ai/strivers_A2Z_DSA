a=[[1,4],[3,2]]
l,r=0,len(a[0])-1
while l<=r:
    cc=l+(r-l)//2
    cm=-1
    cmi=-1
    for i in range(len(a)):
        if a[i][cc]>cm:
            cm=a[i][cc]
            cmi=i
    if (cc==0 and a[cmi][cc]>a[cmi][cc+1]) or (cc==len(a[0])-1 and a[cmi][cc]>a[cm][cc-1]):
        print(cmi,cc)
        break
    elif (cc==0 and a[cmi][cc]<a[cmi][cc+1]) or (cc!=0 and cc!=len(a[0])-1 and a[cmi][cc]<a[cmi][cc+1]):
        l=cc+1
    else:
        h=cc-1

    
