from collections import OrderedDict
from tkinter.constants import N
from typing import List 
import os
from unicodedata import name
import pandas as pd

class TreeNode:
    
    def __init__(self, node_name:str, edges:list):
        self.parent = None
        self.node_name = node_name
        self.node_edges = OrderedDict()
        for edge in edges:
            self.node_edges[edge] = None

    def set_parent(self, parent_node) -> None:
        self.parent=parent_node


    def get_node_name(self) -> str:
        return self.node_name

    def connect_node(self, edge_name, node):
        self.node_edges[edge_name] = node
        node.set_parent(self)

    def __str__(self):
        str = self.node_name + ':\n'
        for node_edge_name, connected_node in self.node_edges.items():
            str = str + f'{node_edge_name} -- {connected_node}'

        return str

    def display_branch(self, tab_idx=0):
        '''
        '''
        # if self.parent == None:
        print('*', ('\t'*tab_idx*2), self.node_name)

        for edge_name, connected_node in self.node_edges.items():

            if connected_node != None:
                print('*',  ('\t'*tab_idx*3), ' - ', edge_name, ' - ')
                connected_node.display_branch( tab_idx+1)

class TreeLeafNode(TreeNode):

    def __init__(self, node_name:str) -> None:
        super(TreeLeafNode, self).__init__(node_name, [])


    def display_branch(self, tab_idx=0):
        print('*',  ('\t'*tab_idx*3),  self.node_name)


class Tree:
    
    def __init__(self) -> None:
        self.root_node:TreeNode = None

    def set_root_node(self, node:TreeNode) -> None:
        self.root_node = node
    
    def __str__(self) -> str:
        return str(self.root_node)
    
    def display(self) -> None:
        self.root_node.display_branch()

class TreeBuilderHelper:
    
    def __init__(self, **kwargs):
        self.node_definitions = {}
        self.leaf_node_definitions = []
        self.output_variable_name = ''

        data_filename =  kwargs.get('data_filename')
        if data_filename != None:
            output_var_name = kwargs.get('output_variable_name')
            self._create_from_dataset(data_filename, output_variable_name=output_var_name)




    def _create_from_dataset(self, data_filename:str, output_variable_name:str=None)->None:
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        dataset_path = os.path.join(current_dir, data_filename)

        df = pd.read_csv(dataset_path)

        for column_name in df.columns:
            unique_values = df[column_name].unique()
            if column_name != output_variable_name:
                self.add_node_definition(column_name, unique_values)
            else:
                self.output_variable_name = column_name

                for unique_value in unique_values:
                    self.add_leafnode_definition(unique_value)

    def __str__(self) -> str:
        res_str = f'''Node Definitions:\n{self.node_definitions}\nLeaf Node Definitions:\n{self.output_variable_name} - {self.leaf_node_definitions}'''
        return res_str


    def add_node_definition(self, node_name:str, edges:List[str]) -> None:
        self.node_definitions[node_name] = edges

    def add_leafnode_definition(self, node_name:str):
        self.leaf_node_definitions.append(node_name)

    def create_node(self, node_name:str) -> TreeNode:
        new_node = TreeNode(node_name, self.node_definitions[node_name])
        return new_node

    def create_leaf_node(self, node_name:str) -> TreeNode:
        
        if not node_name in self.leaf_node_definitions:
            raise('Invalid Node Name. Name not available as leaf node name')
        else:
            new_node = TreeLeafNode(node_name)
            return new_node



if __name__ == "__main__":
    
    helper = TreeBuilderHelper(data_filename='data.csv', output_variable_name='play')

    print(helper)

    a = helper.create_node('outlook')
    b = helper.create_node('temperature')
    c = helper.create_node('windy')

    y = helper.create_leaf_node('yes')
    n = helper.create_leaf_node('no')

    a.connect_node('sunny', b)
    b.connect_node('hot', y)
    a.connect_node('rainy', c)
    c.connect_node('weak', n)

    t = Tree()
    t.set_root_node(a)
    t.display()