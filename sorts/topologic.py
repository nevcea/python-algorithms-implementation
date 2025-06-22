# https://en.wikipedia.org/wiki/Topological_sorting
from collections import defaultdict, deque

def topological_sort_dfs(graph):
  visited = set()
  stack = []

  def dfs(v):
    visited.add(v)

    for neighbor in graph[v]:
      if neighbor not in visited:
        dfs(neighbor)

    stack.append(v)

  for node in graph:
    if node not in visited:
      dfs(node)

  return stack[::-1]

def topological_sort_kahn(graph):
  in_degree = defaultdict(int)
  
  for node in graph:
    for neighbor in graph[node]:
      in_degree[neighbor] += 1
  
    if node not in in_degree:
      in_degree[node] = 0
  
  queue = deque([node for node in in_degree if in_degree[node] == 0])
  sorted_list = []

  while queue:
    node = queue.popleft()
    sorted_list.append(node)

    for neighbor in graph[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)
  
  if len(sorted_list) == len(in_degree):
    return sorted_list
  else:
    return False