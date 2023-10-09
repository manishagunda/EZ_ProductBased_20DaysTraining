'''You are given an array of N integers and another integer K How many
numbers appear in the arrays at least K times?
Standard input
The first line contains two integers N and K.
The second line contains N integers, representing the elements of the array.
Standard output
Print the answer on the first lines
Example:
input:
3 1
1 1 1
output
1
input
5 2
1 2 3 2 1
output
2'''

n,k=map(int,input().split())
lst=[]
c=0
for i in range(n):
    lst.append(int(input()))
s=set(lst)
for i in s:
    if lst.count(i)>=k:
        c+=1
print(c)
    






