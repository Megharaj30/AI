def bfs(visited, graph, queue):
    if not queue:
        return
    else:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

        bfs(visited, graph, queue)

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Taking user input
graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

start_node = input("Enter starting node: ")

# Initialize visited sets and queue
visited = set()
visited1 = set()
queue = [start_node]
visited.add(start_node)

print("\nFollowing is the Depth-First Search:")
dfs(visited1, graph, start_node)

print("\n\nFollowing is the Breadth-First Search:")
bfs(visited, graph, queue)
print()
