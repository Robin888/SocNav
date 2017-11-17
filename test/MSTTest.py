import unittest

from dm.MST import MST
from dm.Move import Move
from dm.State import State


class testMST(unittest.TestCase):
    @unittest.skip
    def testMSTbuild(self):
        curstate1 = State({'f1': 100, 'f2': 100, 'f3': 100}, {'i1:': 0, 'i2': 0, 'i3': 0})
        desState1 = State({'f1': 100, 'f2': 100, 'f3': 100}, {'i1:': 0, 'i2': 0, 'i3': 0})
        curState2 = State({'f1': 0, 'f2': 0, 'f3': 0}, {'i1:': 0, 'i2': 0, 'i3': 0})
        desState2 = State({'f1': 0, 'f2': 0, 'f3': 0}, {'i1:': 0, 'i2': 0, 'i3': 0})
        move1 = Move({"f1": 5, "f2": 10, "f3": 20}, {'i1:': 0, 'i2': 0, 'i3': 0}, [], .5, None)
        move2 = Move({"f1": 100, "f2": 200, "f3": 300}, {'i1:': 0, 'i2': 0, 'i3': 0}, [], .5, None)
        move0 = Move({"f1": 0, "f2": 0, "f3": 0}, {'i1:': 0, 'i2': 0, 'i3': 0}, [], 0, None)
        moves = [move1, move2, move0]
        test_mst1 = MST(curstate1, desState1, moves, 2)

        G = test_mst1.graph
        # nx.draw(test_mst1.graph)
        # plt.show()
        root = test_mst1.tree
        edges = G.edges()
        print(edges)
        edges = [G[node1][node2]['object'] for (node1, node2) in edges]
        self.assertTrue(move2 in edges)

    def testMSTremove(self):
        curstate1 = State({'f1': 0}, {'i1:': 0})
        desState1 = State({'f1': 100}, {'i1:': 100})
        curState2 = State({'f1': 0}, {'i1:': 0})
        desState2 = State({'f1': 0}, {'i1:': 0})
        move1 = Move({"f1": 1}, {'i1:': 0}, [], .5, None)
        move2 = Move({"f1": 2}, {'i1:': 0}, [], .5, None)
        move0 = Move({"f1": 0}, {'i1:': 0}, [], 0, None)
        moves = [move1, move2, move0]
        test_mst1 = MST(curstate1, desState1, moves, 2)
        print(len(test_mst1.getMoves()))
        G = test_mst1.graph
        edges = [G[test_mst1.currentState][childNode]['object'] for childNode in
                 test_mst1.graph.neighbors(test_mst1.currentState)]

        self.assertTrue(move0 in edges)
        self.assertTrue(test_mst1.containsMove(move0))

        test_mst1.removeMove(move0)
        G1 = test_mst1.graph
        # edges = G1.edges()
        # edges = [G1[node1][node2]['object'] for (node1, node2) in edges]
        edges = [G1[test_mst1.currentState][childNode]['object'] for childNode in
                 test_mst1.graph.neighbors(test_mst1.currentState)]

        self.assertFalse(move0 in edges)
        self.assertFalse(test_mst1.containsMove(move0))


# initialize mst with some random current and desired state (these could be different or the same
# depending on the test case)

# to test whether a move is in the tree check MST.getMoves()

# checkout networkx package to see how to check what is in the graph
if __name__ == '__main__':
    unittest.main()
