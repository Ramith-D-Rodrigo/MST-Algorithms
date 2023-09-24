import heapq

class IndexedPriorityQueue:
    def __init__(self):
        self.pq = []    #the priority queue (a min heap)
        #mapping the node index to the index in the priority queue
        self.index = {} 
        #mapping the node index to the edge (weight, source, destination) 
        # (the current minimum edge to the node)
        self.edges = {} 
        
    def empty(self):
        return len(self.pq) == 0
    
    def len(self):
        return len(self.pq)
    
    #node index is the index of the node in the graph, edge is a tuple 
    # (weight, source, destination)
    def push(self, vertexIndex, edge): 
        #we have to use the weight as the key because the priority queue sorts by key
        if vertexIndex in self.index:
            raise Exception("Node already in priority queue.")
        
        #add the edge to the priority queue
        queueEntry = [edge[2], vertexIndex] #weight, node index
        
        heapq.heappush(self.pq, queueEntry) #add the edge to the priority queue
        self.index[vertexIndex] = queueEntry #add the node index to the index dictionary
        self.edges[vertexIndex] = edge #add the edge to the edge dictionary
        
    def pop(self):
        if self.empty():
            raise Exception("Priority queue is empty.")
        
        #pop the edge with the minimum weight
        weight, vertexIndex = heapq.heappop(self.pq)
        
        edge = self.edges[vertexIndex]
        #remove the node index from the index dictionary
        del self.index[vertexIndex]
        del self.edges[vertexIndex]
        
        return vertexIndex, edge
    
    def decreaseKey(self, vertexIndex, edge):
        if vertexIndex not in self.index:
            raise Exception("Node not in priority queue.")
        
        #update the edge in the edge dictionary
        
        if edge[2] < self.index[vertexIndex][0]:
            self.index[vertexIndex][0] = edge[2]
            self.edges[vertexIndex] = edge
            heapq.heapify(self.pq) 
    
    
    def contains(self, vertexIndex):
        return vertexIndex in self.index
    