class Graph:
    def __init__(self, graphType, VertexList, edgeList):
        self.adjacencyMatrix = None
        self.adjacencyList = None  # dest, weight
        self.graphType = graphType

        if graphType == 0:  # adjacency matrix
            # create a 2D list of size len(VertexList) x len(VertexList)
            vertexLen = len(VertexList)
            self.adjacencyMatrix = [[float('inf')] * vertexLen for _ in range(vertexLen)]


            # populate adjacency matrix with edgeList
            for i in range(len(edgeList)): 
                #the graph is undirected, so we add the edge in both directions
                self.adjacencyMatrix[edgeList[i][0]][edgeList[i][1]] = edgeList[i][2]
                self.adjacencyMatrix[edgeList[i][1]][edgeList[i][0]] = edgeList[i][2]

        elif graphType == 1:  # adjacency list
            # create a list of size len(VertexList)
            self.adjacencyList = [[] for _ in range(len(VertexList))]

            # populate adjacency list with edgeList
            for i in range(len(edgeList)):  
                if(edgeList[i][0] == edgeList[i][1]): #no self loops
                    continue
                
                # the graph is undirected, so we add the edge in both directions
                self.adjacencyList[edgeList[i][0]].append((edgeList[i][1], edgeList[i][2]))
                self.adjacencyList[edgeList[i][1]].append((edgeList[i][0], edgeList[i][2]))

        else:
            print("Invalid graph type.")

    def getGraphType(self):
        return self.graphType

    def printGraph(self):
        if self.adjacencyMatrix is not None:  # adjacency matrix
            for row in self.adjacencyMatrix:
                print("\t".join(str(weight) if weight != float('inf') else "-" for weight in row))
        elif self.adjacencyList is not None:  # adjacency list
            for i, adjacency in enumerate(self.adjacencyList):
                print(f"{i}: " + " ".join(f"({dest},{weight})" for dest, weight in adjacency))
        else:
            print("Invalid graph type.")

    def getEdgeCount(self):
        return len(self.edgeList)