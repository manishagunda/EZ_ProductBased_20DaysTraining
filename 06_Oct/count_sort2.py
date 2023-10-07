def count_sort(l):
    s=len(l)
    count_arr=[0]*s
    result_arr=[0]*s
    for i in range(s):
        count_arr[l[i]]+=1
    print("count array:",count_arr)
    for i in range(1,s):
        count_arr[i]+=count_arr[i-1]
    print("updated array:",count_arr)
    n=s-1
    for n in range(n,-1,-1):
        result_arr[count_arr[l[n]]-1]=l[n]
        count_arr[l[n]]-=1
    return result_arr
l=list(map(int,input().split()))
print("sorted array",count_sort(l))