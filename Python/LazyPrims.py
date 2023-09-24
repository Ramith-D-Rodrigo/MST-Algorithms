from queue import PriorityQueue

class LazyPrims:
    def __init__(self, graph, startingVertex):
        self.visited = []
        self.minimumSpanningTree = set()
        self.pq = PriorityQueue()
        
        if graph.getGraphType() == 0 :# adjacency matrix
            #first find the number of vertices
            vertexCount = len(graph.adjacencyMatrix)
            
            self.visited = [False] * vertexCount #keep track of visited vertices
            
            #add the starting vertex to the priority queue
            self.addEdges(graph, startingVertex)
            
            self.createMST(graph, vertexCount - 1)  #edge count is one less than the vertex count
        
        elif graph.getGraphType() == 1: #adjacency list
            vertexCount = len(graph.adjacencyList)
            
            self.visited = [False] * vertexCount #keep track of visited vertices
            
            #add the starting vertex to the priority queue
            self.addEdges(graph, startingVertex)
            
            self.createMST(graph, vertexCount - 1) #edge count is one less than the vertex count
          
    def createMST(self, graph, edgeCount):
        #while the priority queue is not empty
        while not self.pq.empty() and len(self.minimumSpanningTree) != edgeCount:
            edge = self.pq.get() #get the edge with the minimum weight (weight, source, destination)
            
            destination = edge[2] #get the destination vertex
            
            if(self.visited[destination] == True): #if already visited, skip
                continue
            
            self.minimumSpanningTree.add((edge[1], edge[2], edge[0])) #add the edge to the minimum spanning tree (source, destination, weight)
            
            self.addEdges(graph, destination) #add the edges of the destination vertex to the priority queue  
    
    
    def addEdges(self, graph, vertex):
        if graph.getGraphType() == 0: #adjacency matrix
            #mark the vertex as visited
            self.visited[vertex] = True
            
            #go over all the edges of the visited vertex
            for i in range(len(graph.adjacencyMatrix[vertex])):
                if graph.adjacencyMatrix[vertex][i] != float('inf') and self.visited[i] == False:
                    #add the weight first so that the priority queue sorts by weight
                    self.pq.put((graph.adjacencyMatrix[vertex][i], vertex, i)) #(weight, source, destination)
                    #self.pq.put((graph.adjacencyMatrix[vertex][i], i, vertex)) #(weight, source, destination) reverse edge (not needed)
        
        elif graph.getGraphType() == 1:
            self.visited[vertex] = True
            
            for edge in graph.adjacencyList[vertex]:
                if self.visited[edge[0]] == False:
                    self.pq.put((edge[1], vertex, edge[0]))
                    #self.pq.put((edge[1], edge[0], vertex)) no need to add the reverse edge
        
    
    def printMinimumSpanningTree(self):
        for edge in self.minimumSpanningTree:
            print(edge)
        
        