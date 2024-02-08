import numpy as np

class SimpleTree:
    '''
    Simple implementation of a tree structure. The tree uses the following concepts:
    Node: a node in the tree that has edges connecting it to other nodes
    Leaf Node: A terminating Node. Does not have child nodes
    Tree: the connectivity of the nodes
    Root Node: The tree's parent node
    '''

    def __init__(self):
        self.nodes = []
        self.leafnodes = []
        self.tree = np.array([0], dtype=object)
        self.tree = self.tree.reshape((1, 1))
        self.rootnode = None

    def __get_index(self, node):
        '''
        Gets the index of a node from the nodes list
        Arguments:
        ----------

        node - node whose index is required
        '''
        idx = self.nodes.index(node, 0, len(self.nodes))
        return idx

    def add_leafnode(self, node):
        '''
        Adds a leaf node to the tree
        Arguments:
        ----------

        node - the leaf node
        '''
        self.leafnodes.append(node)
        self.add_node(node)

    def add_node(self, node):
        '''
        Adds a new node to the tree.

        Arguments:
        ----------

        node - the new node
        '''
        # a new tree is created with an empty node in the tree array
        # if this is first node, use this node. otherwise extend
        if len(self.nodes) > 0:
            # create a bigger tree - extend by one in all dims
            tree_c = np.zeros(
                (self.tree.shape[0]+1, self.tree.shape[1]+1), dtype=object)
            # assign the iold tree into the new tree
            tree_c[0:self.tree.shape[0], 0:self.tree.shape[1]] = self.tree
            self.tree = tree_c

        self.nodes.append(node)

    def show(self):
        print('nodes:', self.nodes)
        print('leaf nodes:', self.leafnodes)
        print('tree:', self.tree)
        print('root node:', self.rootnode)

    def add_edge(self, parent_node, child_node, edge_name=1):
        '''
        Connects two nodes

        Arguments:
        ----------

        parent_node - the from node

        child_node - the to node

        edge_name - name given to this connection, 1 default
        '''
        p_idx = self.__get_index(parent_node)
        c_idx = self.__get_index(child_node)
        self.tree[p_idx][c_idx] = edge_name
        self.tree[c_idx, p_idx] = edge_name

    def set_root_node(self, root):
        '''
        Sets the root node

        Arguments:
        ----------

        root - the root node
        '''
        self.rootnode = root

    def append_tree(self, receipt_node, new_tree, edge_name=1):
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
            for i in range(idx, len(new_tree.tree[idx, :])):
                # if there is an edge in the new tree create that edge in the current tree
                if new_tree.tree[idx, i] != 0:
                    self.add_edge(
                        new_tree.nodes[idx], new_tree.nodes[i], new_tree.tree[idx, i])

        # create an edge between the receipt node and the root node of the new tree
        self.add_edge(receipt_node, new_tree.rootnode)

    def display(self):
        '''
        displays the tree recursively
        '''
        self.__display_branch(self.__get_index(self.rootnode))

    def __display_branch(self, node_idx, parent_idx=None, tab_idx=0):
        if parent_idx == None:
            print(('\t'*tab_idx), self.nodes[node_idx])
        else:
            print(('\t'*tab_idx*2), ' - ',
                  self.tree[parent_idx, node_idx], ' - ', self.nodes[node_idx])

        tree_filter = self.tree[node_idx, :] != 0
        tree_filter[0:node_idx] = False

        filter_idx = np.nonzero(tree_filter)

        for child_idx in filter_idx[0]:
            self.__display_branch(child_idx, node_idx, tab_idx+1)

    def traverse(self, case):
        '''
        recursively go through the case in hand whilst traversing 
        the tree until the result is found

        Arguments:
        ----------

        case: dictionary containing the case in had in the form 'node:branch'
        '''
        return self.__traverse_step(case, self.rootnode)

    def __traverse_step(self, case, current_node):
        current_node_idx = self.__get_index(current_node)

        tree_branch = self.tree[current_node_idx, :]

        if current_node in case:
            current_value = case[current_node]
        else:
            return None

        value_idx = np.where(tree_branch == current_value)[0].squeeze()

        new_node = self.nodes[value_idx]

        if new_node in self.leafnodes:
            return new_node
        else:
            del case[current_node]
            return self.__traverse_step(case, new_node)

if __name__=='__main__':
    a_tree = SimpleTree()
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

    b_tree = SimpleTree()
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