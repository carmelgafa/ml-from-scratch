'''
simple example demonstrating the operation of the SimpleTree

1. creates a tree with nodes and edges
2. creates another tree with nodes and edges
3. appends the second tree to the first tree 
'''
from nary_tree import NAryTree

t = NAryTree()

t.add_node('a1')
t.add_node('a2')
t.add_node('a3')
t.add_node('a4')
t.add_node('a5')

t.add_edge('a1', 'a2', 'aa')
t.add_edge('a1', 'a3', 'ab')
t.add_edge('a2', 'a4', 'ac')
t.add_edge('a2', 'a5', 'ad')

t.generate_rules()