def undirected_builder(edges):
    graph = {}
    
    for a,b in edges:
        if a not in graph:
            graph[a] = []
            
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    return graph

def directed_builder(edges):
    
    graph = {}

    #list of tuples, destructure each into the a, b. a = src, b = dst
    for a,b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        
    return graph

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_builder(edges))