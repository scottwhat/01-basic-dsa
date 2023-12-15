def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def undirected_path(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if undirected_path(graph, neighbor, dst, visited) == True:
            return True

    return False


edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]


undirected_path(edges, 'm', 'j', set())  # -> True
