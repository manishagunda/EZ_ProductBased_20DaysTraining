r=int(input("Enter no of the rows:"))
c=int(input("Enter no of the columns:"))
matrix=[]
for i in range(r):
    a=[]
    for i in range(c):
        x=int(input("Enter the item:"))
        a.append(x)
    matrix.append(a)
print("The Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The Clock wise Rotated Matrix is:")
for i in range(r):
    for j in range(c-1,-1,-1):
        print(matrix[j][i],end=" ")
    print()
print("The AntiClock wise Rotated Matrix is:")
for i in range(r-1,-1,-1):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()