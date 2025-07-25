def sum_above_below_left_diagonal(matrix):
    n = len(matrix)
    above = 0
    below = 0

    for i in range(n):
        for j in range(n):
            if j > i:
                above += matrix[i][j]
            elif j < i:
                below += matrix[i][j]

    return above, below


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

above, below = sum_above_below_left_diagonal(matrix)
print("Sum above left diagonal:", above)
print("Sum below left diagonal:", below)
