def kadanes(arr):
    s=float("-inf")
    cs=arr[0]
    n=len(arr)
    for i in range(1,n):
        if cs<0:
            cs=0
        if arr[i]<0:
            s=max(s,cs+arr[i])
        cs=cs+arr[i]
    return max(s,cs)
print(kadanes([-1,-2,-3,-4,-5,18,65,]))