matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m, n = len(matrix), len(matrix[0])
for i in range(n):
    for j in range(m):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
