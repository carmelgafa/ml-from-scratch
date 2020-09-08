from collections import OrderedDict
from typing import List 

class TreeNode:
    
    def __init__(self, node_name:str, edges:[]):
        self.parent = None
        self.node_name = node_name
        self.node_edges = OrderedDict()

        for edge in edges:
            self.node_edges[edge] = []


    def connect_node(self, edge_name, node):
        self.node_edges[edge_name].append(node)


    def __str__(self):
        return f'{self.node_name} : {self.node_edges}'





class Tree:
    
    def __init__(self):
        self.root_node = None

    def add_root_node(self, node):
        self.root_node = node
    
    

class TreeBuilderHelper:
    
    def __init__(self):
        self.node_definitions = {}
        self.leaf_node_definitions = {}

    def add_node_definition(self, node_name:str, edges:List[str]):
        self.node_definitions[node_name] = edges

    def add_leafnode_definition(self, node_name:str, value:str):
        self.node_definitions[node_name] = value

    def __str__(self):
        return f'{self.node_definitions}'

    def create_node(self, node_name:str):
        new_node = TreeNode(node_name, self.node_definitions[node_name])
        return new_node





if __name__ == "__main__":
    
    helper = TreeBuilderHelper()
    helper.add_node_definition('A', ['s1', 's2'])
    helper.add_node_definition('B', ['b2', 'b1', 'ce', 's1', 's2'])
    print(helper)

    a = helper.create_node('A')
    print(a)

    b = helper.create_node('B')
    print(b)

    a.connect_node('s1', b)
    a.connect_node('s2', helper.create_node('B'))
    print(a)

