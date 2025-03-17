import unittest
from mis.dnf import max_independent_set
from mis.graph import Graph

class TestSmallExampleTree(unittest.TestCase):
    def test_small_tree(self):
        tree = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        }
        root = 0
        graph = Graph.from_dict(tree)
        max_set_size = max_independent_set(graph, root)
        self.assertEqual(max_set_size, 3)
