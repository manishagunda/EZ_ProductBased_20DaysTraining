def two_pointer(arr,target):
    arr.sort()
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:
            return True
        if arr[i]+arr[j]<target:
            i+=1
        if arr[i]+arr[j]>target:
            j-=1
    return False
arr = [1, 2, 3, 4, 5, 6, 7]
target = 2
result = two_pointer(arr, target)
print(result)
