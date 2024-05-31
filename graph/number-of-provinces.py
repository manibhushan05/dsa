# https://leetcode.com/problems/number-of-provinces/
from collections import defaultdict, deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)
        count = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                count += 1
                self.bfs(graph, node, visited)
        return count

    def bfs(self, graph, start_node, visited):
        visited.add(start_node)
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
