# def depth_first_print(graph, start):
#     stack = [start]
    
#     while stack:  # while stack is not empty
#         current = stack.pop()
#         print(current)
        
#         # Add all neighbors to the stack
#         for neighbor in graph[current]:
#             stack.append(neighbor)

# Test the function

# def depth_first_print(graph, current):
    
#     print(current)
#     #implicit base case with for loop that hits a dead end
#     for neighbor in graph[current]:
#         depth_first_print(graph, neighbor)

from collections import deque


def breadth_first_print(graph, start):
    
    queue = deque([start])
    
    while len(queue) > 0:
        queue[0] = current
        print(current) 
        queue.popleft()
        
        
        for neighbor in graph[current]:
            queue.append(neighbor)
        
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')