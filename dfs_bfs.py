from collections import deque

# Function to take user input for the graph
def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ").strip()
        neighbours = input(f"Enter neighbours of {node} separated by space: ").strip().split()
        graph[node] = neighbours
    return graph

# DFS Function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Main code
graph = input_graph()
start_node = input("Enter starting node for traversal: ").strip()

print("\nDFS Traversal:")
dfs(graph, start_node)
print("\n\nBFS Traversal:")
bfs(graph, start_node)









# Enter number of nodes: 6
# Enter node name: A
# Enter neighbours of A separated by space: B C
# Enter node name: B
# Enter neighbours of B separated by space: A D E
# Enter node name: C
# Enter neighbours of C separated by space: A F
# Enter node name: D
# Enter neighbours of D separated by space: B
# Enter node name: E
# Enter neighbours of E separated by space: B
# Enter node name: F
# Enter neighbours of F separated by space: C
# Enter starting node for traversal: A


