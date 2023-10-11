def find_triplet(arr, target):
    arr.sort()  # Sort the input array.

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return [arr[i], arr[left], arr[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return None  # If no triplet is found.

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 15
result = find_triplet(arr, target)
if result:
    print("Triplet found:", result)
else:
    print("No triplet found")
