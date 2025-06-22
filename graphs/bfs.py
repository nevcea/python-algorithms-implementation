from collections import deque

def bfs(graph: dict, start_node: int):
  visited = {i: False for i in graph.keys()}
  queue = deque([start_node])
  visited[start_node] = True

  while queue:
    current = queue.popleft()
    print(current, end=" ")

    for next in graph[current]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)