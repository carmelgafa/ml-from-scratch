class Node():
    def __init__(self, name) -> None:
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self) -> str:
        return self.name

class Edge():
    def __init__(self, src, dest) -> None:
        self.src = src
        self.dest = dest
    def get_source(self):
        return self.src
    def get_destination(self):
        return self.dest
    def __str__(self) -> str:
        return f'{self.src.get_name()} -> {self.dest.get_name()}'

class Digraph():
    '''
    edges direction inb only one direction
    options are:
    1. create adjacency matrix joining src to dest
        ok for digraph as it can handle both directions
        not symmetric therefore
        if few edges present a huge matrix with mostly 0
    2. adjacency list for every node have a list of destinations
        nodes keys in dict
    '''
    def __init__(self) -> None:
        self.edges ={}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []

    def add_edge(self, edge:Edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not(src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def  get_children(self, node):
        return self.edges[node]
    
    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self) -> str:
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + f'{src.get_name()} -> {dest.get_name()}\n'
        return result[:-1]

class Graph(Digraph):
    def add_edge(self, edge: Edge):
        Digraph.add_edge(self,edge)
        rev_edge = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev_edge)

