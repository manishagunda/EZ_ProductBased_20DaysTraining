def sum(arr,queries):
    n=len(arr)
    ps=[0 for i in range(n)]
    for i in range(n):
        if i==0:
            ps[i]=arr[i]
        else:
            ps[i]=ps[i-1]+arr[i]
    for query in queries:
        i=query[0]
        j=query[1]
        if i==0:
            print(ps[j],end=" ")
        else:
            print(ps[j]-ps[i-1],end=" ")
query_subarray_sum([2,4,5,1,6,3,7,8],[[0,4],
                      [1,3],[4,6]])
