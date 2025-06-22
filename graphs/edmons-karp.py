from collections import deque

class Graph:
  def __init__(self, size):
    self.matrix = [[0] * size for _ in range(size)]
    self.size = size
    self.vertex_data = [''] * size
  
  def add_edge(self, u, v, c):
    self.matrix[u][v] = c
  
  def add_vertex_data(self, v, d):
    if 0 <= v < self.size:
      self.vertex_data[v] = d
  
  def bfs(self, s, t, parent):
    visited = [False] * self.size
    queue = deque([s])
    visited[s] = True

    while queue:
      u = queue.popleft()

      for i, v in enumerate(self.matrix[u]):
        if not visited[i] and v > 0:
          queue.append(i)
          visited[i] = True
          parent[i] = u

    return visited[t]

  def edmonds_karp(self, source, sink):
    parent = [-1] * self.size
    max_flow = 0

    while self.bfs(source, sink, parent):
      path_flow = float('inf')
      s = sink

      while s != source:
        path_flow = min(path_flow, self.matrix[parent[s]][s])
        s = parent[s]
      
      max_flow += path_flow
      v = sink

      while v != source:
        u = parent[v]
        self.matrix[u][v] -= path_flow
        self.matrix[v][u] += path_flow
        v = parent[v]

      path = []
      v = sink

      while v != source:
        path.append(v)
        v = parent[v]
      
      path.append(source)
      path.reverse()
      path_names = [self.vertex_data[node] for node in path]

      print("Path:", " -> ".join(path_names), ", Flow:", path_flow)
  
    return max_flow 