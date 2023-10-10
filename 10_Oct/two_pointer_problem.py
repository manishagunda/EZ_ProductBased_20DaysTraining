def two_sum_sorted(arr, target):
    left = 0  # Pointer starting from the left (beginning) of the array
    right = len(arr) - 1  # Pointer starting from the right (end) of the array

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]  # Found a pair that sums up to the target
        elif current_sum < target:
            left += 1  # Move the left pointer to the right
        else:
            right -= 1  # Move the right pointer to the left

    return None  # No pair found

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7]
target_sum = 10
result = two_sum_sorted(sorted_array, target_sum)

if result:
    print(f"Pair that sums up to {target_sum}: {result}")
else:
    print("No such pair found.")
