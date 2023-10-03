def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = n // 2, n - 1

    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        
        if magic_square[i][j] != 0:
            j -= 2
            i += 1
            continue
        else:
            magic_square[i][j] = num
            num += 1
        
        j += 1
        i -= 1

    return magic_square

def print_magic_square(square):
    for i in range(len(square)):
        for j in range(len(square[0])):
            print(square[i][j], end="\t")
        print()

n = 3
magic_square = generate_magic_square(n)
print(f"A {n}x{n} Magic Square:")
print_magic_square(magic_square)

def generate_mirror_image(matrix):
    mirror_image = [row[::-1] for row in matrix]
    return mirror_image

def generate_water_image(matrix):
    water_image = matrix[::-1]
    return water_image

mirror_image = generate_mirror_image(magic_square)
water_image = generate_water_image(magic_square)

print("Original Matrix:")
for row in magic_square:
    print(row)

print("\nMirror Image:")
for row in mirror_image:
    print(row)

print("\nWater Image:")
for row in water_image:
    print(row)