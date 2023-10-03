# Initialize a 3x3 magic square with zeros
magic_square = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
n = 3  # Order of the magic square
# Initialize the starting position
i,j = 0, n // 2  # Start in the middle column of the first row
# Fill in the magic square with values from 1 to n^2
for num in range(1, n**2 + 1):
    magic_square[i][j] = num
    # Calculate the next position
    new_i,new_j = (i - 1) % n,(j + 1) % n
    # If the next position is already occupied, move down instead
    if magic_square[new_i][new_j] != 0:
        i = (i + 1) % n
    else:
        i, j = new_i, new_j
# Print the magic square
for row in magic_square:
    for num in row:
        print(f"{num:2d}", end=" ")
    print()