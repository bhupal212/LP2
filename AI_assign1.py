# DFS & BFS (Graph Traversal)

from collections import defaultdict, deque
# DFS Traversal

def dfs(graph,start,visited):
    visited.add(start)
    print(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
            
# BFS Traversal

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
                
# Build Graph

def buildgraph():
    graph = defaultdict(list)

    print("Enter edges in the format 'vertex1 vertex2'. Enter 'done' to finish.")
    while True:
        edge = input("Enter the edge: ").strip()
        if edge.lower() == 'done':
            break
        
        v1,v2 = edge.split()
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return graph

def main():
    graph = buildgraph()
    if not graph:
        print("The graph is empty!")
        
    start_vertex = input("Enter the strting vertex: ").strip()
    
    print("\nDFS:")
    dfs(graph,start_vertex,set())
    
    print("\nBFS:")
    bfs(graph,start_vertex)
    
    
if __name__ == "__main__":
    main()


# Enter edges in the format 'vertex1 vertex2'. Enter 'done' to finish.
# Enter the edge: a b
# Enter the edge: a c
# Enter the edge: a d
# Enter the edge: b e
# Enter the edge: b f
# Enter the edge: c g
# Enter the edge: c h
# Enter the edge: d h
# Enter the edge: done
# Enter start node: a
# DFS: 
# a
# b
# e
# f
# c
# g
# h
# d
# BFS: 
# a
# b
# c
# d
# e
# f
# g
# h

