def sd(nums):
    l,r=0,len(nums)-1
    f=False
    if len(nums)==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[-1]!=nums[-2]:
        return nums[-1]
    while l<=r:
        mid=l+(r-l)//2
        print(l,r,mid)
        if nums[mid]!=nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        if (nums[mid]==nums[mid+1] and mid%2==0)or(nums[mid]==nums[mid-1] and mid%2==1):
            l=mid+1
        else:
            r=mid-1
        
    return -1 

a=[1,1,2,3,3,4,4]
print(sd(a))
