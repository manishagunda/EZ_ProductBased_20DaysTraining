def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half, left_count = count_inversions(left_half)
    right_half, right_count = count_inversions(right_half)

    merged_arr, merge_count = merge_and_count(left_half, right_half)

    total_count = left_count + right_count + merge_count

    return merged_arr, total_count

def merge_and_count(left, right):
    result = []
    count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i  # Count inversions
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, count

# Example usage:
arr = [9,6,8,4]
sorted_arr, inversions = count_inversions(arr)
print("Sorted array is:", sorted_arr)
print("Number of inversions:", inversions)
