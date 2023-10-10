def sliding_window(arr,k):
    _sum=0
    ps=0
    i,j=0,k-1
    while j<len(arr):
        if i==0:
            _sum=sum(arr[i:j+1])
            ps=_sum
            
        else:
            cs=ps-arr[i-1]+arr[j]
            _sum=max(_sum,cs)
            ps=cs
        i+=1
        j+=1
    return _sum
arr=list(map(int,input().split()))
k=int(input())
print(sliding_window(arr,k))
        
