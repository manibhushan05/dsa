from collections import deque


def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue a node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Process the node (in this case, print it)

            # Enqueue all adjacent nodes of the dequeued node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


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
