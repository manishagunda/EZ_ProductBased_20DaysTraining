def merge_inversion (lst):
    global c
    if len(lst) <= 1 :
        return lst
    else:
        mid= len(lst) //2
        left =lst[:mid]
        right=lst[mid:]
        merge_inversion (left)
        merge_inversion (right)
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lst[k] = left[i]
                i+=1
                k+=1
            else:
                lst[k]=right[j]
                c+=len(left)-i
                j+=1
                k+=1
        while i<len(left):
            lst[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            lst[k]=right[j]
            j+=1
            k+=1
    return c
lst=list(map(int,input().split()))
c=0
print(merge_inversion(lst))