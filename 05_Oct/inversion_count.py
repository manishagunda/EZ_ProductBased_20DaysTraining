def count_inversions(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count
arr = list(map(int,input().split()))
inversions = count_inversions(arr)
print("Number of inversions:", inversions)
