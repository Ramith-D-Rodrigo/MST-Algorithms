from IndexedPriorityQueue import IndexedPriorityQueue

class EagerPrims:
    def __init__(self, graph, startingVertex):
        self.visited = []
        self.minimumSpanningTree = set()
        self.ipq = IndexedPriorityQueue()
        
        if graph.getGraphType() == 0 :
            vertexCount = len(graph.adjacencyMatrix)
            self.visited = [False] * vertexCount #keep track of visited vertices
            
            self.relaxEdgesAtNode(graph, startingVertex)
            
            self.createMST(graph, vertexCount - 1)  #edge count is one less than the vertex count
    
        elif graph.getGraphType() == 1:
            vertexCount = len(graph.adjacencyList)
            self.visited = [False] * vertexCount #keep track of visited vertices
            
            self.relaxEdgesAtNode(graph, startingVertex)
            
            self.createMST(graph, vertexCount - 1)  #edge count is one less than the vertex count
    
    def createMST(self, graph, edgeCount):
        while not self.ipq.empty() and len(self.minimumSpanningTree) != edgeCount:
            #get the minimum edge from ipq
            destinationIndex, edge = self.ipq.pop()
            
            self.minimumSpanningTree.add(edge) #add the edge to the minimum spanning tree (source, destination, weight)
            
            self.relaxEdgesAtNode(graph, destinationIndex)
    
    
    def relaxEdgesAtNode(self, graph, vertex):
        #visit the vertex
        self.visited[vertex] = True
        
        #get the edges of the vertex
        if graph.getGraphType() == 0: #adjacency matrix
            for destination in range(len(graph.adjacencyMatrix[vertex])):
                if graph.adjacencyMatrix[vertex][destination] != float('inf'):
                    if self.visited[destination] == True:
                        continue
                    
                    if not self.ipq.contains(destination): #not in the priority queue
                        #then insert
                        self.ipq.push(destination, (vertex, destination, graph.adjacencyMatrix[vertex][destination]))
                    else:
                        #improve the minimum cost edge
                        self.ipq.decreaseKey(destination, (vertex, destination, graph.adjacencyMatrix[vertex][destination]))
                        
        elif graph.getGraphType() == 1:
            for edge in graph.adjacencyList[vertex]:
                destination = edge[0]
                weight = edge[1]
                
                if self.visited[destination] == True:
                    continue
                
                if not self.ipq.contains(destination):
                    self.ipq.push(destination, (vertex, destination, weight))
                else:
                    self.ipq.decreaseKey(destination, (vertex, destination, weight))
                    
    def printMinimumSpanningTree(self):
        for edge in self.minimumSpanningTree:
            print(edge)
        