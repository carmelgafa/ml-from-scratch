'''
simple example demonstrating the operation of the SimpleTree

1. creates a tree with nodes and edges
2. creates another tree with nodes and edges
3. appends the second tree to the forst tree 
'''
from simple_tree import SimpleTree

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

a_tree.append_tree('Five', b_tree)
a_tree.display()
