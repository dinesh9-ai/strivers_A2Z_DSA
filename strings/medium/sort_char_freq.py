def frequencySort(a):
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        q=sorted(d,key=lambda x:d[x])
        #print(d)
        s=''
        for i in q[::-1]:
            s=s+(i)*d[i]
        
        return s
