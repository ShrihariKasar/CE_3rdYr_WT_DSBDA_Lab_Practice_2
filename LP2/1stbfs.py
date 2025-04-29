from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    node = queue.popleft()
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
    bfs_recursive(graph, queue, visited)

# User input
graph = {}
n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting node for BFS: ")
print("BFS traversal:")
visited = set()
visited.add(start)
bfs_recursive(graph, deque([start]), visited)

# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 1stbfs.py                                                                                                                           
# Enter number of edges: 4
# Enter edge (u v): A B
# Enter edge (u v): A C
# Enter edge (u v): B D
# Enter edge (u v): C D
# Enter starting node for BFS: A
# BFS traversal:
# A B C D 
# PS C:\Users\Asus\OneDrive\Desktop\LP2>