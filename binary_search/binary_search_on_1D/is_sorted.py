def arraySortedOrNot(arr, n):
    f=True
    q=arr[0]
    for i in arr[1:]:
        if i<q:
            return 0
        q=i
    return 1
a=[1,2,3,4,5]
