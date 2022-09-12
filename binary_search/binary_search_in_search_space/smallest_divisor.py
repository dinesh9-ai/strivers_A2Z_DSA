def smallestDivisor(nums,threshold):
        l=1
        r=10**6
        while l<=r:
            m=l+(r-l)//2
            t=0
            for i in nums:
                t+=math.ceil(i/m)
            if t>threshold:
                l=m+1
            else:
                r=m-1
        return l
