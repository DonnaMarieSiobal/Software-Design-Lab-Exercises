graph = {
  'A': ['B','C', 'F'],
  'B': ['D', 'E', ],
  'C': ['F'],
  'D': ['G'],
  'E': ['F'],
  'F': [],
  'G': []
}
print("Given graph is:")
print(graph)

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s, end=" ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("\nBreadth First Search traversal of graph with source A is:")
bfs(visited, graph, 'A')

