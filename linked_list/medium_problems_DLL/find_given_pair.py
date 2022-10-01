def findPairsWithGivenSum(self,target):
    d={}
    h=head
    f=[]
    while h:
        if (target-h.data) in d:
            f.append([abs(target-h.data),h.data])

        else:
            d[h.data]=1
        h=h.next
    f.sort(key=lambda x :x[0])
    return f
