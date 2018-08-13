import unittest
import numpy as np
from SimpleTree import SimpleTree

class TestSimpleTree (unittest.TestCase):

    def step_1(self, a_tree):
        '''
        initialization test
        '''
        self.assertEqual(len(a_tree.nodes), 0)
        self.assertEqual(len(a_tree.leafnodes), 0)
        self.assertEqual(len(a_tree.tree), 1)
        self.assertIsNone(a_tree.rootnode)

        return a_tree

    def step_2(self, a_tree):
        '''
        add nodes test
        '''
        a_tree.add_node('One')
        a_tree.add_node('Two')
        a_tree.add_node('Three')
        a_tree.add_node('Four')

        self.assertEqual(len(a_tree.nodes), 4)
        self.assertEqual(a_tree.nodes, ['One', 'Two', 'Three', 'Four'])

        self.assertEqual(len(a_tree.leafnodes), 0)

        np.testing.assert_array_equal(a_tree.tree,  np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=object))

        return a_tree

    def step_3(self, a_tree):
        '''
        edges test
        '''
        a_tree.add_edge('One', 'Three', 'No')
        np.testing.assert_array_equal(a_tree.tree, np.array([[0, 0, 'No', 0], [0, 0, 0, 0], ['No', 0, 0, 0], [0, 0, 0, 0]], dtype=object))

        a_tree.add_node('Five')
        np.testing.assert_array_equal(a_tree.tree, np.array([[0, 0, 'No', 0, 0], 
                                                            [0, 0, 0, 0, 0], 
                                                            ['No', 0, 0, 0, 0], 
                                                            [0, 0, 0, 0, 0],
                                                            [0, 0, 0, 0, 0]], dtype=object))

        a_tree.add_edge('One', 'Two', 'Yes')
        a_tree.add_edge('Two', 'Four', 'Yes')
        a_tree.add_edge('Four', 'Five', 'Yes')

        np.testing.assert_array_equal(a_tree.tree, np.array([[0, 'Yes', 'No', 0, 0], 
                                                            ['Yes', 0, 0, 'Yes', 0], 
                                                            ['No', 0, 0, 0, 0],
                                                            [0, 'Yes', 0, 0, 'Yes'], 
                                                            [0, 0, 0, 'Yes', 0]], dtype=object))


        a_tree.add_node('Six')
        np.testing.assert_array_equal(a_tree.tree, np.array([[0, 'Yes', 'No', 0, 0, 0], 
                                                            ['Yes', 0, 0, 'Yes', 0, 0], 
                                                            ['No', 0, 0, 0, 0, 0],
                                                            [0, 'Yes', 0, 0, 'Yes', 0], 
                                                            [0, 0, 0, 'Yes', 0, 0],
                                                            [0, 0, 0, 0, 0, 0]], dtype=object))


        a_tree.add_edge('Four', 'Six', 'No')
        np.testing.assert_array_equal(a_tree.tree, np.array([[0, 'Yes', 'No', 0, 0, 0], 
                                                            ['Yes', 0, 0, 'Yes', 0, 0], 
                                                            ['No', 0, 0, 0, 0, 0],
                                                            [0, 'Yes', 0, 0, 'Yes', 'No'], 
                                                            [0, 0, 0, 'Yes', 0, 0],
                                                            [0, 0, 0, 'No', 0, 0]], dtype=object))

        return a_tree


    def _steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name) 

    def test_steps(self):

        a_tree = SimpleTree()
        
        for name, step in self._steps():
            try:
                a_tree = step(a_tree)
            except Exception as e:
                self.fail("{} failed ({}: {})".format(name, type(e), e))
