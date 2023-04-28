class Graph():
    def __init__(self, num_nodes, edges, directed = False):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(self.num_nodes)]

        self.weighted = len(edges) > 0 and len(edges[0]) ==3
        self.directed = directed

        self.weights = [[] for _ in  range(self.num_nodes)]

        if self.weighted:
            for n1,n2,weight in edges:
                self.edges[n1].append(n2)
                self.weights[n1].append(weight)

                if not self.directed:
                    self.edges[n2].append(n1)
                    self.weights[n2].append(weight)
        else:
            for n1,n2 in edges:
                self.edges[n1].append(n2)
                if not self.directed:
                    self.edges[n2].append(n1)




    
    def __repr__(self):           #   when we call object directly
        result = ""
        if self.weighted:
            result += "\n".join([f"{node} : {list(zip(neighbors,weight))}" for node, (neighbors,weight) in enumerate(zip(self.edges, self.weights))])
        else:
            result += "\n".join([f"{node} : {neighbors}" for node, neighbors in enumerate(self.edges)])

        return result

    def __str__(self):           # When we call print(graph) or str(graph)
        return self.__repr__()



num_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
graph1 = Graph(num_nodes1, edges1)
print(graph1)
print("")


num_nodes2 = 5                                             
edges2 = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]        
graph2 = Graph(num_nodes2, edges2)
print(graph2)
print("")


num_nodes3 = 9
edges3 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
graph3 = Graph(num_nodes3, edges3)
print(graph3)
print("")

num_nodes4 = 5
edges4 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
graph4 = Graph(num_nodes4, edges4, True)
print(graph4)
print("")
