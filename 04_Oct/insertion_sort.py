import time
start_time = time.time()
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = list(map(int,input().split())) 
insertion_sort(arr)
print("Sorted array is:", arr)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time:",execution_time,"seconds")

