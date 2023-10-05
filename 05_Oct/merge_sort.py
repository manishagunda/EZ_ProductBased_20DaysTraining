def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)
    return sorted_arr

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Compare elements from the left and right subarrays and merge them
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from both subarrays
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Example usage:
arr = list(map(int,input().split()))
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
