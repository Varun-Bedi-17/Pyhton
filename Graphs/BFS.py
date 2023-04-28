class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)
            

    def bfs(self, source):
        visited = [False] * len(self.edges)
        queue = []

        # distance = [None] * len(self.edges)   # To calculate distance from given node(source)
        # parent = [None] * len(self.edges)     # to calaculate parent

        # distance[source] = 0
        
        visited[source] = True    
        queue.append(source)
        i = 0
        
        while i < len(queue):
            for v in self.edges[queue[i]]:
                if not visited[v]:
                    # distance[v] = distance[queue[i]] + 1       # for distance
                    # parent[v] = queue[i]                       # for parent
                    visited[v] = True
                    queue.append(v)
            i += 1
            
        return queue#,distance,parent


    def __repr__(self):           #   when we call object directly
        return "\n".join([f"{node} : {neighbors}" for node, neighbors in enumerate(self.edges)])
    
    def __str__(self):           # When we call print(graph) or str(graph)
        return self.__repr__()

number_of_nodes = 5                                                   # Basic method of graph 
all_edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]         #  but not efficient
graph = Graph(number_of_nodes, all_edges)

print(graph.bfs(3))


graph2 = Graph(4, [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)])
print(graph2.bfs(2))