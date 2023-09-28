def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  
my_array = list(map(int,input().split(" ")))
t= int(input())
result = linear_search(my_array, t)
if result != -1:
    print(f"Element {t} found at index {result}.")
else:
    print(f"Element {t} not found in the array.")