def bellman_ford(graph: dict, vertices, source):
  distances = [float('inf')] * vertices
  distances[source] = 0

  for _ in range(vertices - 1):
    for u, v, w in graph:
      if distances[u] != float('inf') and distances[u] + w < distances[v]:
        distances[v] = distances[u] + w
  
  for u, v, w in graph:
    if distances[u] != float('inf') and distances[u] + w < distances[v]:
      return None

  return distances