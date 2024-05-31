from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)



# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node for BFS traversal
start_node = 'A'

print("BFS Traversal:")
bfs(graph, start_node)
