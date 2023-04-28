class Graph:
    # number of vertices
    __n = 0
  
    # adjacency matrix
    __g =[[0 for x in range(10)] for y in range(10)]
       
    def __init__(self, x):
        self.__n = x

        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__g[i][j]= 0
 
    def displayAdjacencyMatrix(self):
        print("\n\n Adjacency Matrix:", end ="")
        
        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__g[i][j], end ="")

    def addEdge(self, x, y):
        if(x>= self.__n) or (y >= self.__n) or x < 0 or y < 0:
            print("Vertex does not exists !")
          
        if(x == y):
            print("Same Vertex !")
        else:
            self.__g[y][x]= 1
            self.__g[x][y]= 1     
 
    def addVertex(self):
        self.__n = self.__n + 1
           
         # initializing the new elements to 0
        for i in range(0, self.__n):
            self.__g[i][self.__n-1]= 0
            self.__g[self.__n-1][i]= 0 
                             
    def removeVertex(self, x):
        if(x > self.__n):
            print("Vertex not present !")
        else:
            while(x<self.__n):
          
                 # shifting the rows to left side
                for i in range(0, self.__n):
                       self.__g[i][x]= self.__g[i][x + 1]
             
                 # shifting the columns upwards
                for i in range(0, self.__n):
                       self.__g[x][i]= self.__g[x + 1][i]
                x = x + 1

            # decreasing the number of vertices
            self.__n = self.__n - 1

    def removeEdge(self, x, y):
        if (x < 0) or (x >= self.__n):
            print("Vertex {} does not exist!".format(x))
        if (y < 0) or (y >= self.__n):
            print("Vertex {} does not exist!".format(y))
             
        if(x == y):
            print("Same Vertex!")
 
        else:
            self.__g[y][x] = 0
            self.__g[x][y] = 0            
 
 

obj = Graph(4)
      
obj.addEdge(0, 1)
obj.addEdge(0, 2)
obj.addEdge(1, 2)
obj.addEdge(2, 3)
obj.displayAdjacencyMatrix()
  
obj.addVertex()

obj.addEdge(4, 1)
obj.addEdge(4, 3)
obj.displayAdjacencyMatrix()
      
obj.removeVertex(1)
obj.displayAdjacencyMatrix()

obj.removeEdge(1,2)
obj.displayAdjacencyMatrix()
