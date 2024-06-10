matrix_1 = [[1, 2], [3, 4]]
matrix_2 = [[5, 6], [7, 8]]
result = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[0])):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    result.append(row)
print(result)

result = []
m, n, p = len(matrix_1), len(matrix_1[0]), len(matrix_2[0])
for i in range(m):
    row =[]
    for j in range(n):
        val = 0
        for k in range(p):
            val += matrix_1[i][k]* matrix_2[k][j]
        row.append(val)

    result.append(row)
print(result)