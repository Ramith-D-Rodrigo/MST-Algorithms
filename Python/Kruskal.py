from Graph import Graph
from UnionFind import UnionFind

class Kruskal:
    def __init__(self, graph):
        self.minimumSpanningTree = set()

        if graph.getGraphType() == 0:  # Adjacency matrix
            unionFind = UnionFind(list(range(len(graph.adjacencyMatrix))))

            orderedEdgeList = [(x, y, value) for x, row in enumerate(graph.adjacencyMatrix) for y, value in enumerate(row)]
            orderedEdgeList.sort(key=lambda x: x[2])
            orderedEdgeList = [edge for edge in orderedEdgeList if edge[2] != float('inf')] # remove edges with weight infinity

            self.createMST(orderedEdgeList, unionFind)

        elif graph.getGraphType() == 1:  # Adjacency list
            unionFind = UnionFind(list(range(len(graph.adjacencyList))))

            orderedEdgeList = [(x, dest, weight) for x, edges in enumerate(graph.adjacencyList) for dest, weight in edges]
            orderedEdgeList.sort(key=lambda x: x[2])

            self.createMST(orderedEdgeList, unionFind)

    def createMST(self, orderedEdgeList, unionFindStructure):
        for edge in orderedEdgeList:
            if unionFindStructure.find(edge[0]) != unionFindStructure.find(edge[1]):
                self.minimumSpanningTree.add((edge[0], edge[1], edge[2]))
                unionFindStructure.union(unionFindStructure.find(edge[0]), unionFindStructure.find(edge[1]))

    def printMinimumSpanningTree(self):
        for edge in self.minimumSpanningTree:
            print(edge)

