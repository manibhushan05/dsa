def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes

    if start not in visited:
        print(start)  # Process the node (in this case, print it)
        visited.add(start)  # Mark the node as visited

        # Recursively visit all adjacent nodes of the current node
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)


def dfs_iterative(graph, start):
    visited = set()  # Set to keep track of visited nodes
    stack = [start]  # Initialize stack with the starting node

    while stack:
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            print(node)  # Process the node (in this case, print it)
            visited.add(node)  # Mark the node as visited

            # Push all adjacent unvisited nodes onto the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node for DFS traversal
start_node = 'A'

print("DFS Traversal:")
dfs(graph, start_node)
