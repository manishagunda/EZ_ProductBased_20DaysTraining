def find_triplet(arr, target):
    n = len(arr)

    for i in range(n - 2):
        seen = set()  # A set to store pairs of elements.
        current_target = target - arr[i]

        for j in range(i + 1, n):
            if current_target - arr[j] in seen:
                return [arr[i], arr[j], current_target - arr[j]]
            seen.add(arr[j])

    return None  # If no triplet is found.

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 15
result = find_triplet(arr, target)
if result:
    print("Triplet found:", result)
else:
    print("No triplet found")
