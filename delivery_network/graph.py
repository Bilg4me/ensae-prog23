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

    def get_path_with_power(self, src, dest, power):
        comps = self.connected_components()
        comp_connex = [l for l in comps if (src in l) and (dest in l)][0]
        if comp_connex == []:
            return None
        
        
        def tous_devant(x, list):
            return [[x] + l for l in list]

        
        def all_paths(node1, node2, to_visit):
            if node1 == node2:
                return [[node2]]
            
            else:
                print(to_visit)
                to_visit.pop(to_visit.index(node1))
                result=[]
                intersection = [n for n in self.neighbors(node1) if n in to_visit]
                for (node,p_min,d) in self.graph[node1]:
                    if node in intersection and power >= p_min:
                        
                        result += tous_devant(node1 , all_paths(node, node2, to_visit))
                
                return result

        
        """
        Finding the shortest path in term of distance among all the path convenient for the power
        """
        
        def min_dist(all_paths):
            # path = [1,2,3]
            min_d = 0
            min_path = []
            for path in all_paths:
                dist = 0
                for k in range(len(path) - 1):
                    for (n,p,d) in self.graph[path[k]]:
                        if n == self.graph[path[k+1]][0]:
                            dist += d
                if dist <= min_d:
                    min_d = dist
                    min_path = path

            return (min_d, min_path)
        
        return min_dist(all_paths(src,dest,comp_connex))

    def neighbors(self, node):
        return [neighbor for (neighbor, p, d) in self.graph[node]]

    def connected_components(self):
        visited = {node: False for node in self.nodes}
        connex_comp = []
        # parcours en profondeur d'une composante connexe

        def dfs(comp):
            if comp == []:
                return []
            elif visited[comp[0]]:  # le premier element a été visité
                return dfs(comp[1:])
            else:
                visited[comp[0]] = True
                return [comp[0]] + dfs(self.neighbors(comp[0]) + comp[1:])

        for node in self.nodes:
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

    g = Graph([ (i+1) for i in range(nb_nodes)])
    
    for line in network[1:]:
        line = line.split(' ')
        if len(line) == 4 :
            [node1, node2, pow_min, dist] = [int(line[0]), int(line[1]), int(line[2]), int(line[3])]
            g.add_edge(node1, node2, pow_min, dist)
        else:
            [node1, node2, pow_min] = [int(line[0]), int(line[1]), int(line[2])]
            g.add_edge(node1, node2, pow_min)
            
    return g



g = graph_from_file("c:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/network.03.in")
print(g)
g.get_path_with_power(1,2, 14)
