from typing import List


# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
def count_squares(self, matrix: List[List[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    res = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        res[i][0] = matrix[i][0]
    for i in range(n):
        res[0][i] = matrix[0][i]
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                res[i][j] = min(res[i - 1][j], res[i - 1][j - 1], res[i][j - 1]) + 1
    count = 0
    for i in range(m):
        for j in range(n):
            count += res[i][j]
    return count
