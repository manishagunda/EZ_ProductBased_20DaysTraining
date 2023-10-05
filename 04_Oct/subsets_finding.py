nums = [6, 8, 9, 5, 4, 3, 26, 2]
target_sum = 13
subsets = []
for i in range(2 ** len(nums)):
    # Initialize an empty list for the current subset
    subset = []
    for j in range(len(nums)):
        # Check if the j-th bit in the binary representation of i is set to 1
        if (i >> j) & 1:
            # If the bit is set, add the corresponding element from nums to the subset
            subset.append(nums[j])

    # Check if the sum of the current subset equals the target sum
    if sum(subset) == target_sum:
        # If the sum matches the target, add the subset to the list of subsets
        subsets.append(subset)

# Print the subsets that meet the criteria
if subsets:
    for subset in subsets:
        print(subset)
else:
    print("No subsets found that sum up to the target.")