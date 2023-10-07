def counting_sort(arr):
    if not arr:
        return arr

    # Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)

    # Create a count array to store the count of each element
    count = [0] * (max_val - min_val + 1)
    

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num - min_val] += 1
    print("count array:",count)

    # Reconstruct the sorted array from the count array
    sorted_arr = []
    for i, count_i in enumerate(count):
        sorted_arr.extend([i + min_val] * count_i)

    return sorted_arr

arr = [1,3,2,1,3,0,5,1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
