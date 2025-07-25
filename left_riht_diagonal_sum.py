def diagonal_sums(matrix):
    n = len(matrix)
    left_sum = 0
    right_sum = 0
    for i in range(n):
        left_sum += matrix[i][i]
        right_sum += matrix[i][n - 1 - i]
    return left_sum, right_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

left, right = diagonal_sums(matrix)
print("Left Diagonal Sum:", left)
print("Right Diagonal Sum:", right)
