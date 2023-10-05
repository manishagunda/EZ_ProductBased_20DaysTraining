def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

# Example usage:
arr = list(map(int,input().split()))
bubble_sort(arr)
print("Sorted array is:", arr)
