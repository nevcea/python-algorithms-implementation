def dfs(graph: dict, start_node: int):
  visited = {i: False for i in graph.keys()}

  def search(current: int):
    visited[current] = True
    print(current, end=" ")
    for next in graph[current]:
      if not visited[next]:
        search(next)

  search(start_node)