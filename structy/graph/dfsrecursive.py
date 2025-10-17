def print_graph(graph):
    for node in graph:
        print(f"{node} -> {' '.join(graph[node])}")

# Simple connected graph
graph1 = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# Cyclic graph
graph2 = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['5'],
    '4': ['6', '1'],  # Creates cycle back to 1
    '5': ['6'],
    '6': []
}

# Disconnected components
graph3 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
    # Disconnected component
    'X': ['Y'],
    'Y': ['Z'],
    'Z': ['X']
}

# Complex graph with multiple paths
graph4 = {
    'start': ['a', 'b', 'c'],
    'a': ['d', 'e'],
    'b': ['d', 'f'],
    'c': ['f'],
    'd': ['end'],
    'e': ['end'],
    'f': ['end'],
    'end': []
}

# Graph with self-loops and multiple edges
graph5 = {
    '1': ['1', '2', '2'],  # Self-loop and duplicate edge
    '2': ['3', '4'],
    '3': ['4', '5'],
    '4': ['2'],  # Creates cycle
    '5': ['5']   # Self-loop
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')  # Print for visualization
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Only run tests if file is run directly
if __name__ == "__main__":
    print("Testing graph1:")
    dfs(graph1, 'a')  # Expected: a b d f c e

    print("\nTesting graph2:")
    dfs(graph2, '1')  # Expected: 1 2 4 6 5 3

    print("\nTesting graph3 (component A):")
    dfs(graph3, 'A')  # Expected: A B D C

    print("\nTesting graph4:")
    dfs(graph4, 'start')  # Expected: start a d end e b f c

# List what should be importable from this module
__all__ = ['graph1', 'graph2', 'graph3', 'graph4', 'graph5', 'dfs']

