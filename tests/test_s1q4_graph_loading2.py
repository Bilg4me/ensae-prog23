# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("c:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/network.03.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)

    def test_network1(self):
        g = graph_from_file("c:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/network.1.in")
        self.assertEqual(g.nb_nodes, 20)
        self.assertEqual(g.nb_edges, 100)
        self.assertEqual(g.graph[1][0][2], 6312)
        

if __name__ == '__main__':
    unittest.main()
