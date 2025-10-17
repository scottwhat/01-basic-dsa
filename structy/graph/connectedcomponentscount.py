#return the number of connected components

def connected_components_count(graph):
    #count how many compoennts are in a graph.
    #a component is just a path that hasnt beenn visited 
    #i want to go down a path,
    #check that its a new unique path. if it has already been visited return false
    #explore all nodes
    
    visited = set()
    count = 0
    for node in graph:
       if explore(node, graph, visited) == True:
           count += 1
           
    return count


def explore(current, graph, visited):
    
    if current in visited:
        return False
    
    visited.add(current) 
    for neighbor in graph[current]:
        explore(neighbor, graph, visited)
    
    sdfaaareturn True
    