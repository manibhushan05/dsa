# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from collections import defaultdict, deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        count = 0
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
