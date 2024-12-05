from scc import find_SCC
import unittest

class TestFindSCC(unittest.TestCase):
    def get_tranpose(self, graph):
        n = len(graph)
        transpose = [[] for _ in range(n)]

        for node in range(n):
            for neighbor in graph[node]:
                transpose[neighbor].append(node)
        return transpose

    def check_same_scc(self, scc1, scc2):
        scc1_set = set(tuple(sorted(scc)) for scc in scc1)
        scc2_set = set(tuple(sorted(scc)) for scc in scc2)

        return scc1_set == scc2_set

    def test_random_graph1(self):
        graph = [[1, 3], [2], [3], [0, 2]]
        graph_tranpose = self.get_tranpose(graph)

        scc1 = find_SCC(graph)
        scc2 = find_SCC(graph_tranpose)

        self.assertTrue(self.check_same_scc(scc1, scc2))

    def test_random_graph2(self):
        graph = [[1, 2], [3], [0], [1, 2]]
        graph_tranpose = self.get_tranpose(graph)

        scc1 = find_SCC(graph)
        scc2 = find_SCC(graph_tranpose)

        self.assertTrue(self.check_same_scc(scc1, scc2))

    def test_random_graph3(self):
        graph = [[1, 3], [2], [4], [0], [1]]
        graph_tranpose = self.get_tranpose(graph)

        scc1 = find_SCC(graph)
        scc2 = find_SCC(graph_tranpose)

        self.assertTrue(self.check_same_scc(scc1, scc2))

    def test_random_graph4(self):
        graph = [[1], [2], [], [4], [0]]
        graph_tranpose = self.get_tranpose(graph)

        scc1 = find_SCC(graph)
        scc2 = find_SCC(graph_tranpose)

        self.assertTrue(self.check_same_scc(scc1, scc2))