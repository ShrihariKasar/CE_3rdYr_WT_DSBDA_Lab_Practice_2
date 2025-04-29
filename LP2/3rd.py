import heapq

# Selection Sort (Greedy)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Job Scheduling Problem (Greedy)
def job_scheduling(jobs):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    
    result = [None] * n  # Result stores the jobs that are scheduled
    slot = [-1] * n      # Slot array to keep track of used slots

    # Iterate through all jobs
    for i in range(n):
        # Find a free slot for this job
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if slot[j] == -1:
                slot[j] = i
                result[j] = jobs[i]
                break

    return [job[0] for job in result if job is not None]

# Dijkstra's Algorithm (Single-Source Shortest Path Problem)
def dijkstra(graph, start):
    # Priority queue to store (distance, vertex) pairs
    pq = [(0, start)]  # Start with distance 0 for the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if the node has already been processed
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Kruskal's Minimum Spanning Tree Algorithm
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def kruskal_mst(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))

    return mst

# Prim's Minimum Spanning Tree Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        min_heap = [(0, 0)]
        mst_set = set()
        mst_weight = 0
        mst_edges = []
        key = {i: float('inf') for i in range(self.V)}
        key[0] = 0
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if u in mst_set:
                continue
            mst_set.add(u)
            mst_weight += weight
            if weight != 0:
                mst_edges.append((prev_u, u, weight))  # noqa: F821
            for v, w in self.graph[u]:
                if v not in mst_set and w < key[v]:
                    key[v] = w
                    heapq.heappush(min_heap, (w, v))
                    prev_u = u
        return mst_edges, mst_weight


# Main Menu to Choose Algorithm
def main():
    while True:
        print("\nChoose an algorithm to run:")
        print("1. Selection Sort")
        print("2. Job Scheduling Problem")
        print("3. Dijkstra's Shortest Path")
        print("4. Kruskal's Minimum Spanning Tree")
        print("5. Prim's Minimum Spanning Tree")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':  # Selection Sort
            arr = list(map(int, input("Enter the array to sort (space-separated): ").split()))
            sorted_arr = selection_sort(arr)
            print("Sorted array:", sorted_arr)

        elif choice == '2':  # Job Scheduling Problem
            jobs = []
            n = int(input("Enter number of jobs: "))
            for _ in range(n):
                job = input("Enter job name, deadline, and profit (space-separated): ").split()
                jobs.append((job[0], int(job[1]), int(job[2])))
            scheduled_jobs = job_scheduling(jobs)
            print("Scheduled jobs:", scheduled_jobs)

        elif choice == '3':  # Dijkstra's Shortest Path Problem
            vertices = int(input("Enter the number of vertices: "))
            graph = {}
            for i in range(vertices):
                graph[i] = []
            edges = int(input("Enter number of edges: "))
            for _ in range(edges):
                u, v, weight = map(int, input("Enter edge (u v weight): ").split())
                graph[u].append((v, weight))
            start = int(input("Enter the source vertex: "))
            distances = dijkstra(graph, start)
            print("Shortest distances from source:", distances)

        elif choice == '4':  # Kruskal's Minimum Spanning Tree
            vertices = int(input("Enter number of vertices: "))
            edges = []
            edge_count = int(input("Enter number of edges: "))
            for _ in range(edge_count):
                u, v, weight = map(int, input("Enter edge (u v weight): ").split())
                edges.append((u, v, weight))
            mst = kruskal_mst(vertices, edges)
            print("Minimum Spanning Tree:", mst)

        elif choice == '5':  # Prim's Minimum Spanning Tree
            vertices = int(input("Enter number of vertices: "))
            g = Graph(vertices)
            edges = int(input("Enter number of edges: "))
            for _ in range(edges):
                u, v, weight = map(int, input("Enter edge (u v weight): ").split())
                g.add_edge(u, v, weight)
            mst_edges, mst_weight = g.prim_mst()
            print("Minimum Spanning Tree edges:", mst_edges)
            print("Total weight of MST:", mst_weight)

        elif choice == '6':  # Exit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
    
    
    
    
    
# OUTPUT:-
# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 3rd.py

# Choose an algorithm to run:
# 1. Selection Sort
# 2. Job Scheduling Problem
# 3. Dijkstra's Shortest Path
# 4. Kruskal's Minimum Spanning Tree
# 5. Prim's Minimum Spanning Tree
# 6. Exit
# Enter your choice (1-6): 1
# Enter the array to sort (space-separated): 22 11 3 4 5
# Sorted array: [3, 4, 5, 11, 22]

# Choose an algorithm to run:
# 1. Selection Sort
# 2. Job Scheduling Problem
# 3. Dijkstra's Shortest Path
# 4. Kruskal's Minimum Spanning Tree
# 5. Prim's Minimum Spanning Tree
# 6. Exit
# Enter your choice (1-6):