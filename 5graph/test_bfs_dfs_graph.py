import unittest
from bfs_dfs_graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_vertex('D')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'D')

    def test_print_graph(self):
        expected_output = "A : ['B']\nB : ['A', 'C']\nC : ['B', 'D']\nD : ['C']\n"
        self.assertEqual(self.graph.print_graph(), expected_output)

    def test_add_vertex(self):
        self.assertFalse(self.graph.add_vertex('A'))  # Vertex already exists
        # Vertex added successfully
        self.assertTrue(self.graph.add_vertex('E'))

    def test_add_edge(self):
        # Vertex 'E' does not exist
        self.assertFalse(self.graph.add_edge('A', 'E'))
        # Edge added successfully
        self.assertTrue(self.graph.add_edge('A', 'D'))

    def test_remove_edge(self):
        self.assertFalse(self.graph.remove_edge('A', 'E')
                         )  # Vertex 'E' does not exist
        # Edge removed successfully
        self.assertTrue(self.graph.remove_edge('A', 'B'))

    def test_remove_vertex(self):
        # Vertex 'E' does not exist
        self.assertFalse(self.graph.remove_vertex('E'))
        # Vertex removed successfully
        self.assertTrue(self.graph.remove_vertex('A'))

    def test_dfs(self):
        expected_output = "A B C D "
        self.assertEqual(self.graph.dfs('A'), expected_output)

    def test_bfs(self):
        expected_output = "A B C D "
        self.assertEqual(self.graph.bfs('A'), expected_output)

    def test_is_cyclic(self):
        self.assertFalse(self.graph.is_cyclic())  # Graph is acyclic

    def test_topological_sort(self):
        expected_output = "A B C D "
        self.assertEqual(self.graph.topological_sort(), expected_output)

    def test_is_connected(self):
        self.assertTrue(self.graph.is_connected())  # Graph is connected

    def test_bfs_search(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.bfs_search('A', 'D'))
        self.assertFalse(self.graph.bfs_search('A', 'E')
                         )  # Vertex 'E' does not exist

    def test_dfs_search(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.dfs_search('A', 'D'))
        self.assertFalse(self.graph.dfs_search('A', 'E')
                         )  # Vertex 'E' does not exist

    def test_shortest_path(self):
        expected_output = ['A', 'B', 'C', 'D']
        self.assertEqual(self.graph.shortest_path('A', 'D'), expected_output)
        self.assertIsNone(self.graph.shortest_path(
            'A', 'E'))  # Vertex 'E' does not exist

    def test_get_first_node(self):
        self.assertEqual(self.graph.get_first_node(), 'A')  # First node is 'A'

    def test_bfs_search_from_first(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.bfs_search_from_first('D'))
        self.assertFalse(self.graph.bfs_search_from_first('E')
                         )  # Vertex 'E' does not exist

    def test_dfs_search_from_first(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.dfs_search_from_first('D'))
        self.assertFalse(self.graph.dfs_search_from_first('E')
                         )  # Vertex 'E' does not exist


if __name__ == '__main__':
    unittest.main()


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_vertex('D')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'D')

    def test_print_graph(self):
        expected_output = "A : ['B']\nB : ['A', 'C']\nC : ['B', 'D']\nD : ['C']\n"
        self.assertEqual(self.graph.print_graph(), expected_output)

    def test_add_vertex(self):
        self.assertFalse(self.graph.add_vertex('A'))  # Vertex already exists
        # Vertex added successfully
        self.assertTrue(self.graph.add_vertex('E'))

    def test_add_edge(self):
        # Vertex 'E' does not exist
        self.assertFalse(self.graph.add_edge('A', 'E'))
        # Edge added successfully
        self.assertTrue(self.graph.add_edge('A', 'D'))

    def test_remove_edge(self):
        self.assertFalse(self.graph.remove_edge('A', 'E')
                         )  # Vertex 'E' does not exist
        # Edge removed successfully
        self.assertTrue(self.graph.remove_edge('A', 'B'))

    def test_remove_vertex(self):
        # Vertex 'E' does not exist
        self.assertFalse(self.graph.remove_vertex('E'))
        # Vertex removed successfully
        self.assertTrue(self.graph.remove_vertex('A'))

    def test_dfs(self):
        expected_output = "A B C D "
        self.assertEqual(self.graph.dfs('A'), expected_output)

    def test_bfs(self):
        expected_output = "A B C D "
        self.assertEqual(self.graph.bfs('A'), expected_output)

    def test_is_cyclic(self):
        self.assertFalse(self.graph.is_cyclic())  # Graph is acyclic

    def test_topological_sort(self):
        expected_output = "A B C D "
        self.assertEqual(self.graph.topological_sort(), expected_output)

    def test_is_connected(self):
        self.assertTrue(self.graph.is_connected())  # Graph is connected

    def test_bfs_search(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.bfs_search('A', 'D'))
        self.assertFalse(self.graph.bfs_search('A', 'E')
                         )  # Vertex 'E' does not exist

    def test_dfs_search(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.dfs_search('A', 'D'))
        self.assertFalse(self.graph.dfs_search('A', 'E')
                         )  # Vertex 'E' does not exist

    def test_shortest_path(self):
        expected_output = ['A', 'B', 'C', 'D']
        self.assertEqual(self.graph.shortest_path('A', 'D'), expected_output)
        self.assertIsNone(self.graph.shortest_path(
            'A', 'E'))  # Vertex 'E' does not exist

    def test_get_first_node(self):
        self.assertEqual(self.graph.get_first_node(), 'A')  # First node is 'A'

    def test_bfs_search_from_first(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.bfs_search_from_first('D'))
        self.assertFalse(self.graph.bfs_search_from_first('E')
                         )  # Vertex 'E' does not exist

    def test_dfs_search_from_first(self):
        # Path exists from 'A' to 'D'
        self.assertTrue(self.graph.dfs_search_from_first('D'))
        self.assertFalse(self.graph.dfs_search_from_first('E')
                         )  # Vertex 'E' does not exist


if __name__ == '__main__':
    unittest.main()
