class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for neighbor in self.adj_list[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend(set(self.adj_list[vertex]) - visited)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def is_cyclic(self):
        visited = {v: False for v in self.adj_list}
        for v in self.adj_list:
            if not visited[v]:
                if self.is_cyclic_util(v, visited, -1):
                    return True
        return False

    def topological_sort_util(self, v, visited, stack):
        visited.add(v)
        for i in self.adj_list[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = set()
        stack = []
        for v in self.adj_list:
            if v not in visited:
                self.topological_sort_util(v, visited, stack)
        print(" ".join(stack))

    def is_connected(self):
        visited = set()
        for start_vertex in self.adj_list:
            self.dfs(start_vertex, visited)
            if len(visited) != len(self.adj_list):
                return False
            visited.clear()
        return True

    def bfs_search(self, start_vertex, search_value):
        if start_vertex not in self.adj_list:
            return False

        visited = set()
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex == search_value:
                return True
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.adj_list[vertex]) - visited)

        return False

    def dfs_search(self, start_vertex, search_value, visited=None):
        if visited is None:
            visited = set()

        if start_vertex == search_value:
            return True

        visited.add(start_vertex)

        for neighbor in self.adj_list[start_vertex]:
            if neighbor not in visited:
                if self.dfs_search(neighbor, search_value, visited):
                    return True

        return False

    def get_first_node(self):
        # This returns the first node based on the dictionary's current state.
        # You might want to sort the keys if you need a specific "first" node.

        print(next(iter(self.adj_list)) if self.adj_list else None)
        return next(iter(self.adj_list)) if self.adj_list else None

    def bfs_search_from_first(self, search_value):
        start_vertex = self.get_first_node()
        return self.bfs_search(start_vertex, search_value) if start_vertex else False

    def dfs_search_from_first(self, search_value):
        start_vertex = self.get_first_node()
        return self.dfs_search(start_vertex, search_value) if start_vertex else False

    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.adj_list or end_vertex not in self.adj_list:
            return None

        visited = set()
        # Queue of tuples (vertex, path)
        queue = [(start_vertex, [start_vertex])]

        while queue:
            current_vertex, path = queue.pop(0)

            if current_vertex == end_vertex:
                return path

            if current_vertex not in visited:
                visited.add(current_vertex)

                for neighbor in self.adj_list[current_vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None  # Path not found


graph = Graph()
# Assume you have already added vertices and edges to the graph
search_value = 'C'

# Add vertices to the graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Add edges to the graph
graph.add_edge('A', 'B')

graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Test the bfs_search_from_first and dfs_search_from_first methods
search_value = 'C'
found_in_bfs = graph.bfs_search_from_first(search_value)
print(found_in_bfs)


start_vertex = 'A'
end_vertex = 'D'
path = graph.shortest_path(start_vertex, end_vertex)
