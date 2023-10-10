def square_root_binary_search(x, precision=0.00001):
    if x < 0:
        raise ValueError("Input must be a non-negative number")
    if x == 0 or x == 1:
        return x

    left = 0
    right = x
    while right - left > precision:
        mid = (left + right) / 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid
        else:
            right = mid

    return (left + right) / 2

# Example usage:
number = 16
result = square_root_binary_search(number)
print(f"The square root of {number} is approximately {result:.5f}")
