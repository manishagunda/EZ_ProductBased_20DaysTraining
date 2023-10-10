'''a=[1,2,3,4]
[1],[2],[3],[4]
[1,2],[2,3],[3,4]
[1,2,3],[2,3,4]
[1,2,3,4]
 eg. k=3 i.e.3 numbered subarrays are [1,2,3]
 and [2,3,4], from these max sum is 9 produced
 by [2,3,4]
 total num sub arrays for given array size n
 is n*(n+1)/2'''
def max_subarray_sum(arr, k):
    n = len(arr)
    if k <= 0 or k > n:
        return None  # Invalid input

    max_sum = float('-inf')  # Initialize max_sum as negative infinity

    for i in range(n - k + 1):
        subarray = arr[i:i + k]  # Create a subarray of size k
        current_sum = sum(subarray)  # Calculate the sum of the subarray
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater

    return max_sum

# Example usage:
arr = list(map(int,input().split()))
k = int(input())
result = max_subarray_sum(arr, k)

if result is not None:
    print(f"The maximum sum of {k}-numbered subarrays is: {result}")
else:
    print("Invalid input or k is out of range.")
