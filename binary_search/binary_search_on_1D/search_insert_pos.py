def si(nums, target):
    print(target)
    if target <nums[0]:
        return 0
    elif target>nums[-1]:
        return len(nums)
    l,h=0,len(nums)-1
    r=0
    while l<=h:
        m=l+(h-l)//2
        if target==nums[m]:
            return m
        elif nums[m]<target:
            l=m+1
            r=m
        elif nums[m]>target:
            h=m-1
        
    return r
a=[1,3,5,6]
print(si(a,5))
