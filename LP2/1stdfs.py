def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# User input
graph = {}
n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting node for DFS: ")
print("DFS traversal:")
dfs(graph, start, set())


# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 1stdfs.py                                                                                                                           
# Enter number of edges: 4
# Enter edge (u v): A B
# Enter edge (u v): A C
# Enter edge (u v): B D
# Enter edge (u v): C D
# Enter starting node for DFS: A
# BFS traversal:
# A B C D 
# PS C:\Users\Asus\OneDrive\Desktop\LP2> 