import numpy as np
matrix = np.array([
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9],
    
])
n = matrix.shape[0] # row = 5
for layer in range(n // 2):
    start = layer
    end = n - layer
    left = start
    right = end - 1
    while left < right:
        temp = matrix[start, left]
        matrix[start, left] = matrix[start, right]
        matrix[start, right] = temp
        left += 1
        right -= 1
    top = start
    bottom = end - 1
    while top < bottom:
        temp = matrix[top, start]
        matrix[top, start] = matrix[bottom, start]
        matrix[bottom, start] = temp
        top += 1
        bottom -= 1
for row in matrix:
    print(','.join(map(str, row)))
