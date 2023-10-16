def permute(arr):
    if len(arr)==1:
        return [arr]
    ans=[]
    for i in range(len(arr)):
        t_arr=[arr[i]]
        s_arr=arr[0:i]+arr[i+1:]
        p_arr=permute(s_arr)
        for i in p_arr:
            ans.append(t_arr+i)
    return ans
arr=[1,2,3]
print(permute(arr))