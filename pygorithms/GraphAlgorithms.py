import heapq
import numpy as np

def dijkstraAlgorithm(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def bellmanFordAlgorithm(graph, V, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    for _ in range(V - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] != float('infinity') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] != float('infinity') and distances[u] + w < distances[v]:
                return None
    return distances

def floydWarshallAlgorithm(matrix):
    V = len(matrix)
    dist = list(map(lambda i: list(map(lambda j: j, i)), matrix))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def primAlgorithm(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst

def tarjanAlgorithm(): 
    index = 0
    stack = []
    on_stack = {u: False for u in graph}
    indices = {u: None for u in graph}
    lowlink = {u: None for u in graph}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] is None:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v: break
            sccs.append(scc)

    for v in graph:
        if indices[v] is None:
            strongconnect(v)
    return sccs

def pageRank():
    N = links.shape[0]
    M = links / np.sum(links, axis=0, where=links!=0) 
    v = np.ones(N) / N  
    tele = (1 - d) / N  
    for _ in range(num_iterations):
        v = d * M @ v + tele
    return v



