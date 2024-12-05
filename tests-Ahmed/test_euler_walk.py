from euler_walk import euler_walk
import unittest


class TestEulerWalk(unittest.TestCase):
    def check_valid_euler_path(self, n, adj, path):
        adj_copy = [[adj[i][j] for j in range(n)] for i in range(n)]
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            adj_copy[u][v] -= 1
            adj_copy[v][u] -= 1
        for i in range(n):
            for j in range(n):
                if adj[i][j]:
                    return False
        return True

    def test_euler_walk_zero_nodes(self):
        n = 0
        adj = []
        result = euler_walk(n, adj)

        self.assertEqual(result, None)

    def test_euler_walk_unconnected_even_degree(self):
        n = 4
        adj = [[0, 2, 0, 0], [2, 0, 0, 0], [0, 0, 0, 2], [0, 0, 2, 0]]
        result = euler_walk(n, adj)

        self.assertEqual(result, None)

    def test_euler_walk_unconnected_two_odd_degree(self):
        n = 4
        adj = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 2], [0, 0, 2, 0]]
        result = euler_walk(n, adj)

        self.assertEqual(result, None)

    def test_euler_walk_connected_bad_degree(self):
        n = 4
        adj = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
        result = euler_walk(n, adj)

        self.assertEqual(result, None)

    def test_euler_walk_connected_all_even_degree(self):
        n = 3
        adj = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        result = euler_walk(n, adj)

        self.assertTrue(self.check_valid_euler_path(n, adj, result))

    def test_euler_walk_connected_two_odd_degree(self):
        n = 3
        adj = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        result = euler_walk(n, adj)

        self.assertTrue(self.check_valid_euler_path(n, adj, result))