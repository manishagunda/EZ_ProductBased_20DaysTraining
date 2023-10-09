'''problem:#1 (Two Sum Problem)
arr[]=(2,3,5,7,10,12,15,20),target-19
Answer: 4,6 positions
Explanation :return i and j th pointer positions whose sum of indexed values
equals to target.'''

arr=list(map(int, input().split()))
t=int(input())
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if t==arr[i]+arr[j]:
            print(i+1,j+1)
            break
