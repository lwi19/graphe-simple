import unittest
"""
    graphe_test.py  
    Created by lwi19
    Copyright © 2020 Louis Plouffe. All rights reserved.
"""
"""
Test module for graph_theory 

Call method: python3 -m unittest discover  -p "*test.py" -s ./tests -v
Graphs are imported in this file, 

"""

# import util.graph_lib as glb
from data.some_of_them import g_01, g_02, g_03, g_06, g_07, g_08


class Testfunctions(unittest.TestCase):

    def test_vertices(self):
        """
        Test the presence of a vertices list in a graph.
        :return: True if the list match.
        """
        stuff_to_find = {5, 1, 2, 4, 0, 3}
        stuff_calculated = g_01.vertices
        self.assertSetEqual(stuff_to_find, stuff_calculated,
                            f"error: vertices(), {stuff_to_find} is not expected")

    def test_edges(self):
        """
        Test de presence of list of edges in a graph.
        :return: True if the list match
        """
        edges_tuple = (0, 3), (1, 2), (2, 3), (2, 4)
        stuff_to_find = set(edges_tuple)
        stuff_calculated = g_01.edges()
        self.assertSetEqual(stuff_to_find, stuff_calculated,
                            f"error: edges(), {stuff_to_find} is not expected")

    def test_is_edge(self):
        """
        Test several vertices in a graph.
        :return: True if they exist in a graph.
        """
        stuff_to_find_1 = (18, 19)
        stuff_to_find_2 = (19, 18)
        stuff_to_find_3 = (88, 151)  # this vertex must not pass the test
        self.assertTrue(g_02.is_edge(*stuff_to_find_1),  f"error: is_edges() {stuff_to_find_1} is not expected")
        self.assertTrue(g_02.is_edge(*stuff_to_find_2),  f"error: is_edges() {stuff_to_find_2} is not expected")
        self.assertFalse(g_02.is_edge(*stuff_to_find_3), f"error: is_edges() {stuff_to_find_3} is not expected")

    def test_breadth_or_depth(self):
        """
        Test two different methods of searching: BFS and DFS. They
        must return the same extraction path.
        :return:
        """
        # "ATTENTION: DFS is very long to calculate for a large graph"

        dfs_components = g_06.extract_components(style="DFS")[0]
        bfs_components = g_06.extract_components(style="BFS")[0]
        self.assertTrue([set(i) for i in dfs_components.values()] ==
                        [set(j) for j in bfs_components.values()],
                        "error: DFS and BFS mismatch")

    def test_find_shortest_path(self):
        """
        Test shortest path between two random vertices.
        The calculation is verified in the two possible direction
        They must return the same extraction path
        :return: True if the same result.
        """
        # Do the calculation on two distinct random numbers.
        # TODO: ensure that the vertices are connected (in the same components)

        if rep := g_06.two_random_vertices():
            vertex_one, vertex_two = rep
            if path_in_order := g_06.find_shortest_path(vertex_one, vertex_two):
                if path_in_reverse_order := g_06.find_shortest_path(vertex_two, vertex_one).reverse():
                    print(path_in_order)
                    print(path_in_reverse_order)
                    self.assertEqual(path_in_order, path_in_reverse_order, "error : shortest path miscalculation ")
            else:
                # path_in_order is False when no path exist.
                self.assertTrue(path_in_order, f"error: no possible path between vertices {vertex_one} and {vertex_two}")
        else:
            # rep is False when vertices do not exist in the path
            self.assertTrue(rep, f"error: no valid vertices found")

    # Starting now, all method with pattern test*z could modified graphs.
    # the 'z' is used to ensure the execution after others methods
    # because graphs are modified.

    def test_z_add_edge(self):
        """
        Test the possibility to add an edge
        :return: True if it is added correctly
        """
        # g_01 is modified here
        node_to_add = (5, 1)
        g_01.add_edge(*node_to_add)
        self.assertTrue(g_01.is_edge(*node_to_add), "edge cannot be added")
        node_to_add = (0, "X")
        g_01.add_edge(*node_to_add)
        self.assertFalse(g_01.is_edge(*node_to_add), "ERROR: impossible edge are added ?")

    def test_z_delete_edge(self):
        """
        Test the possibility to delete an edge
        :return: True if it is deleted correctly
        """
        # g_03 is modified here
        edge_to_delete = (4, 5)
        edge_exist = g_03.is_edge(*edge_to_delete)
        g_03.delete_edge(*edge_to_delete)
        self.assertTrue(edge_exist, "cannot delete edge")
        self.assertFalse(g_03.is_edge(*edge_to_delete))

    def test_z_delete_vertex(self):
        """
        Test the possibility to delete one vertex
        :return: True if it is deleted correctly
        """

        # g3 is modified here
        # not only the vertex is deleted, but also all edges connected edge to it.
        vertex_to_delete = g_03.one_random_vertex()
        self.assertTrue(vertex_to_delete in g_03.graph_dict.keys(), f"{vertex_to_delete} vertex is not part of the graph.")
        g_03.delete_vertex(vertex_to_delete)
        self.assertFalse(vertex_to_delete in g_03.graph_dict.keys())
        # when deleted, a vertex must not appear ine the adjacency list.
        self.assertFalse(bool([k for k in g_03.graph_dict.values() if vertex_to_delete in k]))


if __name__ == "__main__":
    unittest.main()
