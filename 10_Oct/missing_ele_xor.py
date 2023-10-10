n=int(input())
arr=list(map(int,input().split()))
x=0
for i in range(1,n+1):
    x=x^i
    if i !=n:
        x=x^arr[i-1]
print(x)

'''for i in range(len(arr)):
    x=x^arr[i]
print(x)'''