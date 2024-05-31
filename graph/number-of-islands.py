# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    result += 1
                    self.bfs(grid, i, j)
        return result

    def bfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        grid[i][j] = "0"
        self.bfs(grid, i + 1, j)
        self.bfs(grid, i - 1, j)
        self.bfs(grid, i, j + 1)
        self.bfs(grid, i, j - 1)
