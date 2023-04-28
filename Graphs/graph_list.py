#                    THIS METHOD IS USED ONLY INTEGER NODES STARTING FROM 0                      #

class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)

    def addEdge(self, src, dest):
        self.edges[src].append(dest)
        self.edges[dest].append(src)

    def removeEdge(self, src, dest):
        self.edges[src].remove(dest)
        self.edges[dest].remove(src)
            
    def __repr__(self):           #   when we call object directly
        return "\n".join([f"{node} : {neighbors}" for node, neighbors in enumerate(self.edges)])
    
    def __str__(self):           # When we call print(graph) or str(graph)
        return self.__repr__()

number_of_nodes = 5                                                   # Basic method of graph 
all_edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]         #  but not efficient
graph = Graph(number_of_nodes, all_edges)

print(graph)      # Call str
print("")

graph.addEdge(0,3)
print(graph)
print("")

graph.removeEdge(0,3)
print(graph)
print("")

graph.removeEdge(1,4)
print(graph)
print("")

# edges = [("A","E"), ("A","E"), ("B","C"), ("B","D"), ("B","E"), ("C","D"), ("D","E")]
# print(Graph(number_of_nodes, edges))     #   ERROR
