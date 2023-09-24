class UnionFind:
    def __init__(self, VertexList):
        # Initialize parent array
        self.parent = list(range(len(VertexList))) 

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)