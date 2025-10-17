def longest_path(graph):
    distance = {}
    
    #find the terminal nodes in graph. the nodes with a 0 len neighbors array 
    #
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0
            
    for node in graph:
        traverse_distance(graph, node, distance)
        
    return max(distance.values())

def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]
    
    largest = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance)
        if attempt > largest:
            largest = attempt
    
    distance[node] = 1 + largest
    return distance[node]

def test_longest_path():
    # Test case 1: Linear path
    graph1 = {
        'a': ['b'],
        'b': ['c'],
        'c': ['d'],
        'd': []
    }
    print("\nTest 1 - Linear path:")
    print(f"Graph: {graph1}")
    print(f"Expected: 3, Got: {longest_path(graph1)}")  # a->b->c->d = 3 edges

    # Test case 2: Multiple paths of different lengths
    graph2 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d', 'e'],
        'd': ['f'],
        'e': ['f'],
        'f': []
    }
    print("\nTest 2 - Multiple paths:")
    print(f"Graph: {graph2}")
    print(f"Expected: 3, Got: {longest_path(graph2)}")  # Paths: a->b->d->f or a->c->d->f or a->c->e->f (all length 3)

    # Test case 3: Single node
    graph3 = {
        'a': []
    }
    print("\nTest 3 - Single node:")
    print(f"Graph: {graph3}")
    print(f"Expected: 0, Got: {longest_path(graph3)}")

    # Test case 4: Complex DAG with multiple paths
    graph4 = {
        'start': ['a', 'b', 'c'],
        'a': ['d'],
        'b': ['d', 'e'],
        'c': ['e', 'f'],
        'd': ['g'],
        'e': ['g', 'h'],
        'f': ['h'],
        'g': ['end'],
        'h': ['end'],
        'end': []
    }
    print("\nTest 4 - Complex DAG:")
    print(f"Graph: {graph4}")
    print(f"Expected: 4, Got: {longest_path(graph4)}")  # start->c->e->h->end = 4 edges

    # Test case 5: Diamond shape
    graph5 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': []
    }
    print("\nTest 5 - Diamond shape:")
    print(f"Graph: {graph5}")
    print(f"Expected: 2, Got: {longest_path(graph5)}")  # a->b->d or a->c->d = 2 edges

def visualize_path(graph, start):
    """Helper function to visualize paths in the graph"""
    def dfs(node, path):
        if len(graph[node]) == 0:
            print(" -> ".join(path))
            return
        for neighbor in graph[node]:
            dfs(neighbor, path + [neighbor])
    
    dfs(start, [start])

if __name__ == "__main__":
    test_longest_path()
    
    print("\nBonus - Path Visualization for graph2:")
    graph2 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d', 'e'],
        'd': ['f'],
        'e': ['f'],
        'f': []
    }
    print("All possible paths from 'a' to 'f':")
    visualize_path(graph2, 'a')

