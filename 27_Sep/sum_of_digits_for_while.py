# using for loop
n=int(input())
temp=n
k=0
for i in range(1,n,n//10):
    x=temp%10
    k=k+int(x)
    temp=temp/10
print(k)

#using while loop
n=int(input())
k=0
while(n>0):
    x=n%10
    k=k+x
    n=n/10
print(int(k))
