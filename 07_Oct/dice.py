'''You have two special dice with 6 faces, each. For each dice you know the
numbers written on each face.You roll the two dices at the same time, and
you add up the numbers showing on the upper faces. What is the most probable
sum value you'll get?
Standard input
The first line contains 6 integers representing the numbers on the first dice.
The second line contains 6 integers representing the numbers on the second dice.
Standard output
Print the answer on the first line. If the solution is not unique,
print the smallest one.
Constraints and notes
The numbers on the dice are integers between 1 and 50
Example:
input:
123456
123456
output:7'''
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c = [0] * 36
for i in range(0,len(l)):
    for j in range(0,len(m)):
        c[l[i]+m[j]+1]+=1
print(max(c))
        





