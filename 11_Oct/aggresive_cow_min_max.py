def can_place_cows(stalls, num_cows, min_distance):
    count = 1  # Number of cows placed in the first stall
    last_position = stalls[0]  # Position of the last placed cow

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_distance:
            count += 1
            last_position = stalls[i]

    return count >= num_cows

def aggressive_cow(stalls, num_cows):
    stalls.sort()  # Sort the stalls in ascending order
    low = 0
    high = stalls[-1] - stalls[0]  # Maximum possible distance

    while low < high:
        mid = (low + high + 1) // 2

        if can_place_cows(stalls, num_cows, mid):
            low = mid
        else:
            high = mid - 1

    return low

# Example usage
stalls = [1, 2, 4, 8, 9]
num_cows = 3
result = aggressive_cow(stalls, num_cows)
print("Maximum minimum distance: ", result)
