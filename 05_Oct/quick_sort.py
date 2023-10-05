def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element (middle element in this case)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort the left and right partitions
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = list(map(int,input().split()))
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
