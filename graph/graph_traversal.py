# Iterative
def dfs(graph, start):
  visited, stack = set(), [start]
  while stack:
    node = stack.pop()
    visited.add(node)
    for neighbor in graph[node]:
      if not neighbor in visited:
        stack.append(neighbor)
  return visited

# Return path
def dfs_path(graph, src, dst):
  stack = [(src, [src])]
  visited = set()
  while stack:
    node, path = stack.pop()
    if node in visited:
      continue
    if node == dst:
      return path
    visited.add(node)
    for neighbor in graph[node]:
      stack.append((neighbor, path + [neighbor]))
  return None

# Recursive
def dfs(graph, start):
  def dfs_recursive(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
      if not neighbor in visited:
        dfs_recursive(graph, neighbor, visited)
  visited = set()
  return dfs_recursive(graph, start, visited)

def bfs(graph, start):
  visited, queue = set(), deque([start])
  while queue:
    node = queue.popleft()
    visited.add(node)
    for neighbor in graph[node]:
      if not neighbor in visited:
          queue.append(neighbor)
  return visited

# Return path
def bfs_path(graph, src, dst):
  visited, queue = set(), deque([[src]])
  while queue:
    path = queue.popleft()
    node = path[-1]
    if node in visited:
      continue
    if node == dst:
      return path
    for neighbor in graph[node]:
      queue.append(path + [neighbor])
  return None

# Topological sort
# Current node comes before any of its neighbor
def top_sort(graph):
  def dfs_recursive(graph, start, visited, sorted_nodes)
    visited.add(start)
    for neighbor in graph[start]:
      if not neighbor in visited:
        dfs_recursive(graph, neighbor, visited)
    sorted_nodes.appendleft(start)

  sorted_nodes, visited = deque(), set()
  for node in graph:
    dfs_recursive(graph, node, visited, sorted_nodes)
  return sorted_nodes