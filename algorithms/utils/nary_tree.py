import numpy as np

class NAryTree:
    '''
    Simple implementation of an n-ary tree structure. The tree uses the following concepts:

    Node: a node in the tree that has edges connecting it to other nodes
    Tree: the connectivity of the nodes. connections are unidirectional.
    Root Node: The tree's parent node
    '''

    def __init__(self):

        self.nodes = []
        # create tree structure with size (1,1)
        # so to have a root node
        self.edges = np.array([0], dtype=object)
        self.edges = self.edges.reshape((1, 1))
        self.rootnode = None
        self.rulebase = []

    def __get_index(self, node) -> int:
        '''
        Gets the index of a node from the nodes list

        Arguments:
        ----------
        node - node whose index is required
        '''
        idx = self.nodes.index(node)
        return idx

    def get_order() -> int:
        pass
        
    def __str__(self) -> str:
        return  f'{self.nodes}\n{str(self.edges)}'

    def add_node(self, node):
        '''
        Adds a new node to the tree.
        If this is the first node, it will be the root node

        Arguments:
        ----------
        node - the new node
        '''

        if node in self.nodes:
            return

        # a new tree is created with an empty node in the tree array
        # if this is first node, use this node. otherwise extend
        if len(self.nodes) > 0:
            # create a bigger tree - extend by one in all dims
            tree_c = np.zeros(
                (self.edges.shape[0]+1, self.edges.shape[1]+1), dtype=object)

            # copy contents of the old tree into the new tree
            tree_c[0:self.edges.shape[0], 0:self.edges.shape[1]] = self.edges

            self.edges = tree_c
        else:
            self.rootnode = node

        self.nodes.append(node)

    def show(self):
        print('nodes:', self.nodes)
        # print('leaf nodes:', self.leafnodes)
        print('tree:', self.edges)
        print('root node:', self.rootnode)

    def add_edge(self, parent_node, child_node, edge_name):
        '''
        Connects two nodes

        Arguments:
        ----------
        parent_node - the from node
        child_node - the to node
        edge_name - name given to this connection, 1 default
        '''

        # print(parent_node, '--->', edge_name, '--->', child_node)

        p_idx = self.__get_index(parent_node)
        c_idx = self.__get_index(child_node)
        self.edges[c_idx][p_idx] = edge_name
        # self.tree[c_idx, p_idx] = edge_name

    def set_root_node(self, root):
        '''
        Sets the root node

        Arguments:
        ----------
        root - the root node
        '''
        self.rootnode = root

    def append_tree(self, receipt_node, new_tree, edge_name='hello'):
        '''
        Appends a tree to the current tree

        Arguments:
        ----------
        receipt_node -  node in current tree to which appended_tree is attached. The root
                        node of the new tree is attached to this node
        new_tree -      the new tree to be attached to the current tree
        edge_name -     the name of the edge connecting the trees
        '''
        # go through all nodes of the new tree and add them to the current tree
        for new_node in new_tree.nodes:
            self.add_node(new_node)

        # now, go again through all the nodes
        for idx, new_node in enumerate(new_tree.nodes):
            # for each node go through rest of nodes
            for i in range(idx, len(new_tree.tree[:, idx])):
                # if there is an edge in the new tree create that edge in the current tree
                if new_tree.tree[i, idx] != 0:
                    for edge in new_tree.tree[i, idx]:

                        self.add_edge(
                            new_tree.nodes[idx], new_tree.nodes[i], edge)

        # create an edge between the receipt node and the root node of the new tree
        self.add_edge(receipt_node, new_tree.rootnode, edge_name)

    def display(self):
        '''
        displays the tree recursively
        '''
        self.__display_branch(self.__get_index(self.rootnode))

    def __display_branch(self, node_idx, parent_idx=None, tab_idx=0):
        '''
        '''        
        if parent_idx == None:
            print('*', ('\t'*tab_idx), self.nodes[node_idx])
        else:
            print('*',  ('\t'*tab_idx*2), ' - ',
                  self.edges[node_idx, parent_idx], ' - ', self.nodes[node_idx])

        tree_filter = self.edges[:, node_idx] != 0

        filter_idx = np.nonzero(tree_filter)

        for child_idx in filter_idx[0]:
            self.__display_branch(child_idx, node_idx, tab_idx+1)


    def generate_rules(self):
        self.__gererate_rule(self.__get_index(self.rootnode), [])
        return self.rulebase


    def __gererate_rule(self, node_idx, rule):

        tree_filter = self.edges[:, node_idx] != 0
        filter_idx = np.nonzero(tree_filter)

        for child_idx in filter_idx[0]:

            # leaf node detection. is child a leaf
            child_filter = self.edges[:, child_idx] != 0
            child_filter_idx = np.nonzero(child_filter)

            c_rule = rule.copy()

            if len(child_filter_idx[0]) == 0:
                ante = f'{self.nodes[node_idx]} is  {self.edges[child_idx, node_idx]}'
                cons = f'output is {self.nodes[child_idx]}'
                
                c_rule.append(ante)
                c_rule.append(cons)
                self.rulebase.append(c_rule)

            else:
                ante = f'{self.nodes[node_idx]} is  {self.edges[child_idx, node_idx]}'
                c_rule.append(ante)
                self.__gererate_rule(child_idx, c_rule)


if __name__=='__main__':
    a_tree = NAryTree()
    a_tree.add_node('One')
    a_tree.add_node('Two')
    a_tree.add_node('Three')
    a_tree.add_node('Four')
    a_tree.add_edge('One', 'Three', 'No')
    a_tree.add_node('Five')
    a_tree.add_edge('One', 'Two', 'Yes')
    a_tree.add_edge('Two', 'Four', 'Yes')
    a_tree.add_edge('Four', 'Five', 'Yes')
    a_tree.add_node('Six')
    a_tree.add_edge('Four', 'Six', 'No')

    a_tree.set_root_node('One')
    a_tree.display()

    b_tree = NAryTree()
    b_tree.add_node('Uno')
    b_tree.add_node('Due')
    b_tree.add_node('Tre')
    b_tree.add_node('Quattro')
    b_tree.add_edge('Uno', 'Due', 'Si')
    b_tree.add_edge('Uno', 'Tre', 'No')
    b_tree.add_edge('Tre', 'Quattro', 'Si')
    b_tree.set_root_node('Uno')
    b_tree.display()

    a_tree.append_tree('Five', b_tree, 'No')
    a_tree.display()