import heapq

class Node:
  def __init__(self, name, g, h):
    self.name = name
    self.g, self.h = g, h
    self.f = g + h
    self.parent = None

  def __lt__(self, other):
    return self.f < other.f

def a_star(start, goal, graph, heuristic):
  open_list = []
  closed_list = set()

  start_node = Node(start, 0, heuristic[start])

  heapq.heappush(open_list, start_node)

  while open_list:
    current_node = heapq.heappop(open_list)

    if current_node.name == goal:
      path = []
      while current_node:
        path.append(current_node.name)
        current_node = current_node.parent
      return path[::-1]

    closed_list.add(current_node.name)

    for neighbor, cost in graph[current_node.name].items():
      if neighbor in closed_list:
        continue

      g, h = current_node.g + cost, heuristic[neighbor]
      neighbor_node = Node(neighbor, g, h)
      neighbor_node.parent = current_node

      if not any(n.name == neighbor and n.g <= g for n in open_list):
        heapq.heappush(open_list, neighbor_node)

  return None