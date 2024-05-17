from typing import List


def largest_rectangle_area(heights):
    stack, ans = [], 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            ans = max(ans, H * W)
        stack.append(i)
    return ans


def maximum_rectangle(matrix: List[List[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    histogram = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        if matrix[0][i] == '1':
            histogram[0][i] = 1
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == '1':
                histogram[i][j] = 1 + histogram[i - 1][j]
    maximum_area = 0
    for i in range(m):
        maximum_area = max(maximum_area, largest_rectangle_area(histogram[i]))
    return maximum_area


mat = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(maximum_rectangle(mat))
