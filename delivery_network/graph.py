class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """

        if not (node1 in self.nodes):
            self.nodes.append(node1)
            self.graph[node1] = []
        if not (node2 in self.nodes):
            self.nodes.append(node2)
            self.graph[node2] = []
        self.graph[node1] += [(node2, power_min, dist)]
        self.graph[node2] += [(node1, power_min, dist)]
        
        
        self.nb_edges += 1
        self.nb_nodes = len(self.nodes)

    def get_path_with_power(self, src, dest, power):
        raise NotImplementedError

    def neighbors(self, node):
        return [neighbor for (neighbor, p, d) in self.graph[node]]

    def connected_components(self):
        visited = { node : False for node in self.nodes }
        connex_comp = []
        #parcours en profondeur d'une composante connexe
        def dfs(comp):
            if comp == []:
                return []
            elif visited[comp[0]] : # le premier element a été visité
                return dfs(comp[1:])
            else:
                visited[comp[0]] = True
                return [ comp[0] ] + dfs(self.neighbors(comp[0]) + comp[1:])

        for node in self.nodes :
            if not visited[node]:
               connex_comp += [dfs([node])]
               
        return connex_comp
    

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        network = file.readlines()
    nb_nodes = int(network[0].split(' ')[0])
    
    g = Graph([])
    for line in network[1:] :
        line = line.split(' ')
        [node1,node2,pow_min] = [line[0], line[1], int(line[2])]
        g.add_edge(node1,node2,pow_min)
    return g