def floyd_warshall(graph: list):
  n = len(graph)
  dist = [row[:] for row in graph]

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  return dist