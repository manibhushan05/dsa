from collections import deque


def dfs_adjacency_matrix(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes

    print(start)  # Process the node (in this case, print it)
    visited.add(start)  # Mark the node as visited

    # Iterate over all nodes in the graph
    for node in range(len(graph)):
        # Check if the current node is adjacent to the start node and not visited
        if graph[start][node] == 1 and node not in visited:
            # Recursively call DFS on the adjacent node
            dfs_adjacency_matrix(graph, node, visited)


def bfs_adjacency_matrix(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue a node from the queue
        if node not in visited:
            print(node)  # Process the node (in this case, print it)
            visited.add(node)  # Mark the node as visited

            # Enqueue all adjacent unvisited nodes of the dequeued node
            for neighbor in range(len(graph)):
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)


# Example adjacency matrix representation of a graph
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

# Starting node for DFS and BFS traversal
start_node = 0

print("DFS Traversal (Adjacency Matrix):")
dfs_adjacency_matrix(graph, start_node)

print("\nBFS Traversal (Adjacency Matrix):")
bfs_adjacency_matrix(graph, start_node)
