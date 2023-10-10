def find_missing_and_repeated(arr):
    n = len(arr)

    # XOR all elements in the array and all numbers from 1 to n
    xor_total = 0
    for i in range(1, n + 1):
        xor_total ^= i
    for num in arr:
        xor_total ^= num

    # Find the rightmost set bit in xor_total
    rightmost_set_bit = xor_total & -xor_total

    missing_element = 0
    repeated_element = 0

    # Divide elements into two groups based on the rightmost set bit
    group1 = 0
    group2 = 0
    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            group1 ^= i
        else:
            group2 ^= i
    for num in arr:
        if num & rightmost_set_bit:
            group1 ^= num
        else:
            group2 ^= num

    # Check which group contains the repeated element
    for num in arr:
        if num == group1:
            repeated_element = num
            missing_element = group2
            break
        elif num == group2:
            repeated_element = num
            missing_element = group1
            break

    return missing_element, repeated_element

# Example usage:
arr = [1,2,4,5,6,6,7,8,9,10]
missing, repeated = find_missing_and_repeated(arr)
print(f"The missing element is: {missing}")
print(f"The repeated element is: {repeated}")
