vertices = [0, 1, 2, 3, 4, 5]

edges = [(0,1,1), (0,2,4), (0,5,2), (1,3,1), (1,4,2), (2,4,2), (3,4,4), (4,5,3)]

from Graph import Graph

graph1 = Graph(1, vertices, edges)
graph2 = Graph(0, vertices, edges)

from Kruskal import Kruskal

kruskal1 = Kruskal(graph1)
kruskal2 = Kruskal(graph2)

print("Kruskal:")

print("Adjacency list:")
kruskal1.printMinimumSpanningTree()
print("Adjacency matrix:")
kruskal2.printMinimumSpanningTree()

from LazyPrims import LazyPrims

lazyPrims1 = LazyPrims(graph1, vertices[0])
lazyPrims2 = LazyPrims(graph2, vertices[0])

print("Lazy Prims:")

print("Adjacency list:")
lazyPrims1.printMinimumSpanningTree()
print("Adjacency matrix:")
lazyPrims2.printMinimumSpanningTree()

from EagerPrims import EagerPrims

eagerPrims1 = EagerPrims(graph1, vertices[0])
eagerPrims2 = EagerPrims(graph2, vertices[0])

print("Eager Prims:")

print("Adjacency list:")
eagerPrims1.printMinimumSpanningTree()
print("Adjacency matrix:")
eagerPrims2.printMinimumSpanningTree()