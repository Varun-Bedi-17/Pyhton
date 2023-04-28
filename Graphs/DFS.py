class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)
            

#####################                   Recursive Approach                       ########################
    def dfs(self, source, visited, queue):
        
        visited[source] = True    
        queue.append(source)
        
        for v in self.edges[source]:
            if not visited[v]:
                self.dfs(v, visited, queue)
            
        return queue  


###################                Another approach                  ##################
    def DFS(graph, source):
        visited = [False] * len(graph.edges)
        stack = [source]
        result = []
        
        while len(stack) > 0:
            current = stack.pop()
            if not visited[current]:
                result.append(current)
                visited[current] = True
                for v in graph.edges[current]:
                    stack.append(v)
                    
        return result



    def __repr__(self):           #   when we call object directly
        return "\n".join([f"{node} : {neighbors}" for node, neighbors in enumerate(self.edges)])
    
    def __str__(self):           # When we call print(graph) or str(graph)
        return self.__repr__()

number_of_nodes = 5                                                   # Basic method of graph 
all_edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]         #  but not efficient
graph = Graph(number_of_nodes, all_edges)


visited = [False]*len(graph.edges)
print(graph.dfs(2, visited, []))
print(graph.DFS(2))



graph2 = Graph(4, [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)])
visited2 = [False]*len(graph.edges)
print(graph2.dfs(2, visited2, []))
print(graph2.DFS(2))
