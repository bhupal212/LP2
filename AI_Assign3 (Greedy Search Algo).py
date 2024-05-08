import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        pq = []
        mst = []
        selected = [False] * self.V
        parent = [-1] * self.V
        heapq.heappush(pq, (0, 0))

        while pq:
            weight, u = heapq.heappop(pq)

            if selected[u]:
                continue
            
            selected[u] = True
            
            if parent[u] != -1:
                mst.append((parent[u], u, weight))

            for v, w in self.graph[u]:
                if not selected[v]:
                    heapq.heappush(pq, (w, v))
                    parent[v] = u

        return mst

if __name__ == "__main__":
    num_vertices = int(input("Vertices: "))
    graph = Graph(num_vertices)

    print("Edges (u v weight):")

    while True:
        edge = input().strip()
        if not edge:
            break
        u, v, weight = map(int, edge.split())
        graph.add_edge(u, v, weight)

    mst = graph.prim_mst()

    print("MST Edges:")
    for edge in mst:
        print(f"({edge[0]} - {edge[1]}) weight {edge[2]}")


# Vertices: 5
# Edges (u v weight):
# 0 1 2
# 0 3 4
# 1 2 3
# 1 3 5
# 2 4 6
# <press Enter to finish>

# MST Edges:
# (0 - 1) weight 2
# (1 - 2) weight 3
# (0 - 3) weight 4
# (2 - 4) weight 6

