# https://justkode.kr/algorithm/python-dijkstra/
import heapq

def dijkstra(graph: dict, start_node: int) -> dict:
  distances = {node: float('inf') for node in graph}
  distances[start_node] = 0
  
  queue = []
  heapq.heappush(queue, [distances[start_node], start_node])

  while queue:
    current_dist, current_dest = heapq.heappop(queue)

    if distances[current_dest] < current_dist:
      continue

    for new_dest, new_dist in graph[current_dest].items():
      distance = current_dist + new_dist
      if distance < distances[new_dest]:
        distances[new_dest] = distance
        heapq.heappush(queue, [distance, new_dest])

  return distances