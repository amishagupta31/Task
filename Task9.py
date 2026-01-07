matrix = [
    [1, 2, 3],
    [4, 1, 2],
    [5, 4, 1]
]

 
toeplitz = True
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        if matrix[i][j] != matrix[i-1][j-1]:
            toeplitz = False

print("Toeplitz:", toeplitz)

 
symmetric = matrix == [list(row) for row in zip(*matrix)]
print("Symmetric:", symmetric)

 
row_sums = [sum(row) for row in matrix]
print("Max sum row index:", row_sums.index(max(row_sums)))

 
rotated = list(zip(*matrix[::-1]))
print("Rotated Matrix:")
for r in rotated:
    print(list(r))
