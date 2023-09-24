from Graph import Graph
from sparseGraphEdges import create_sparse_graph_edges
from denseGraphEdges import create_dense_graph_edges


VERTEX_COUNT = 5500
VERBOSE = True

import sys
import time

#first argument is the sparse graph edges file
#second argument is the dense graph edges file

sparseEdgeFilePath = sys.argv[1] if len(sys.argv) == 3 else "../sparseGraphEdges.txt"
denseEdgeFilePath = sys.argv[2] if len(sys.argv) == 3 else "../denseGraphEdges.txt"

if len(sys.argv) != 3:
    #create a graph with 5500 vertices
    vertices = list(range(VERTEX_COUNT))
    if VERBOSE:
        print(f"Creating sparse graph edges with {VERTEX_COUNT} vertices...")
    sparseEdges = create_sparse_graph_edges(vertices)
    
    if VERBOSE:
        print(f"Creating dense graph edges with {VERTEX_COUNT} vertices...")
    denseEdges = create_dense_graph_edges(vertices)
    
    #write the sparse graph edges to a file
    if VERBOSE:
        print("Writing sparse graph edges to file...")
    with open("../sparseGraphEdges.txt", "w") as f:
        for edge in sparseEdges:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
            
    #write the dense graph edges to a file
    if VERBOSE:
        print("Writing dense graph edges to file...")
    with open("../denseGraphEdges.txt", "w") as f:
        for edge in denseEdges:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")




sparseEdges = []
#read the sparse graph edges from a file
if VERBOSE:
    print("Reading sparse graph edges from file...")
with open(sparseEdgeFilePath, "r") as f:
    for line in f:
        sparseEdges.append(tuple(map(int, line.split())))

denseEdges = []
#read the dense graph edges from a file
if VERBOSE:
    print("Reading dense graph edges from file...")
with open(denseEdgeFilePath, "r") as f:
    for line in f:
        denseEdges.append(tuple(map(int, line.split())))

#dense has all the edges 
# (so take the root of the length of the list to get the number of vertices)   
if VERBOSE:
    print("Creating vertices...")  
vertices = list(range(int(len(denseEdges)**0.5)))   
        

# Create graphs

#graphType = 0 for adjacency matrix
if VERBOSE:
    print("Creating sparse graph with adjacency matrix...")
sparseGraphMatrix = Graph(0, vertices, sparseEdges)
if VERBOSE:
    print("Creating dense graph with adjacency matrix...")
denseGraphMatrix = Graph(0, vertices, denseEdges)

#graphType = 1 for adjacency list
if VERBOSE:
    print("Creating sparse graph with adjacency list...")
sparseGraphList = Graph(1, vertices, sparseEdges)
if VERBOSE:
    print("Creating dense graph with adjacency list...")
denseGraphList = Graph(1, vertices, denseEdges)

# Run Kruskal's algorithm for each graph

from Kruskal import Kruskal

#start the timer
if VERBOSE:
    print("Running Kruskal's algorithm on sparse graph with adjacency matrix...")
start = time.time()

#run Kruskal's algorithm on the sparse graph with adjacency matrix
kruskalSparseMatrix = Kruskal(sparseGraphMatrix)

#stop the timer
end = time.time()

kruskalSparseMatrixTime = end - start

#destroy kruskalSparseMatrix
del kruskalSparseMatrix

#start the timer
if VERBOSE:
    print("Running Kruskal's algorithm on dense graph with adjacency matrix...")
start = time.time()

#run Kruskal's algorithm on the dense graph with adjacency matrix
kruskalDenseMatrix = Kruskal(denseGraphMatrix)

#stop the timer
end = time.time()

kruskalDenseMatrixTime = end - start

#destroy kruskalDenseMatrix
del kruskalDenseMatrix

#start the timer
if VERBOSE:
    print("Running Kruskal's algorithm on sparse graph with adjacency list...")
start = time.time()

#run Kruskal's algorithm on the sparse graph with adjacency list
kruskalSparseList = Kruskal(sparseGraphList)

#stop the timer
end = time.time()

kruskalSparseListTime = end - start

#destroy kruskalSparseList
del kruskalSparseList

#start the timer
if VERBOSE:
    print("Running Kruskal's algorithm on dense graph with adjacency list...")
start = time.time()

#run Kruskal's algorithm on the dense graph with adjacency list
kruskalDenseList = Kruskal(denseGraphList)

#stop the timer
end = time.time()

kruskalDenseListTime = end - start

#destroy kruskalDenseList
del kruskalDenseList

# Run Lazy Prim's algorithm for each graph

from LazyPrims import LazyPrims

#start the timer
if VERBOSE:
    print("Running Lazy Prim's algorithm on sparse graph with adjacency matrix...")
start = time.time()

#run Lazy Prim's algorithm on the sparse graph with adjacency matrix
lazyPrimsSparseMatrix = LazyPrims(sparseGraphMatrix, vertices[0])

#stop the timer
end = time.time()

lazyPrimsSparseMatrixTime = end - start

#destroy lazyPrimsSparseMatrix
del lazyPrimsSparseMatrix

#start the timer
if VERBOSE:
    print("Running Lazy Prim's algorithm on dense graph with adjacency matrix...")
start = time.time()

#run Lazy Prim's algorithm on the dense graph with adjacency matrix
lazyPrimsDenseMatrix = LazyPrims(denseGraphMatrix, vertices[0])

#stop the timer
end = time.time()

lazyPrimsDenseMatrixTime = end - start

#destroy lazyPrimsDenseMatrix
del lazyPrimsDenseMatrix

#start the timer
if VERBOSE:
    print("Running Lazy Prim's algorithm on sparse graph with adjacency list...")
start = time.time()

#run Lazy Prim's algorithm on the sparse graph with adjacency list
lazyPrimsSparseList = LazyPrims(sparseGraphList, vertices[0])

#stop the timer
end = time.time()

lazyPrimsSparseListTime = end - start

#destroy lazyPrimsSparseList
del lazyPrimsSparseList

#start the timer
if VERBOSE:
    print("Running Lazy Prim's algorithm on dense graph with adjacency list...")
start = time.time()

#run Lazy Prim's algorithm on the dense graph with adjacency list
lazyPrimsDenseList = LazyPrims(denseGraphList, vertices[0])

#stop the timer
end = time.time()

lazyPrimsDenseListTime = end - start

#destroy lazyPrimsDenseList
del lazyPrimsDenseList

# Run Eager Prim's algorithm for each graph

from EagerPrims import EagerPrims

#start the timer
if VERBOSE:
    print("Running Eager Prim's algorithm on sparse graph with adjacency matrix...")
start = time.time()

#run Eager Prim's algorithm on the sparse graph with adjacency matrix
eagerPrimsSparseMatrix = EagerPrims(sparseGraphMatrix, vertices[0])

#stop the timer
end = time.time()

eagerPrimsSparseMatrixTime = end - start

#destroy eagerPrimsSparseMatrix
del eagerPrimsSparseMatrix

#start the timer
if VERBOSE:
    print("Running Eager Prim's algorithm on dense graph with adjacency matrix...")
start = time.time()

#run Eager Prim's algorithm on the dense graph with adjacency matrix
eagerPrimsDenseMatrix = EagerPrims(denseGraphMatrix, vertices[0])

#stop the timer
end = time.time()

eagerPrimsDenseMatrixTime = end - start

#destroy eagerPrimsDenseMatrix
del eagerPrimsDenseMatrix

#start the timer
if VERBOSE:
    print("Running Eager Prim's algorithm on sparse graph with adjacency list...")
start = time.time()

#run Eager Prim's algorithm on the sparse graph with adjacency list
eagerPrimsSparseList = EagerPrims(sparseGraphList, vertices[0])

#stop the timer
end = time.time()

eagerPrimsSparseListTime = end - start

#destroy eagerPrimsSparseList
del eagerPrimsSparseList

#start the timer
if VERBOSE:
    print("Running Eager Prim's algorithm on dense graph with adjacency list...")
start = time.time()

#run Eager Prim's algorithm on the dense graph with adjacency list
eagerPrimsDenseList = EagerPrims(denseGraphList, vertices[0])

#stop the timer
end = time.time()

eagerPrimsDenseListTime = end - start

#destroy eagerPrimsDenseList
del eagerPrimsDenseList

# Print run times
if VERBOSE:
    print("Printing run times...")
    
print(f"Kruskal Running Times :")    
print(f"\nSparse graph with adjacency matrix: {kruskalSparseMatrixTime} seconds")
print(f"Dense graph with adjacency matrix: {kruskalDenseMatrixTime} seconds")
print(f"Sparse graph with adjacency list: {kruskalSparseListTime} seconds")
print(f"Dense graph with adjacency list: {kruskalDenseListTime} seconds\n")

print(f"Lazy Prims Running Times :")  
print(f"\nSparse graph with adjacency matrix: {lazyPrimsSparseMatrixTime} seconds")
print(f"Dense graph with adjacency matrix: {lazyPrimsDenseMatrixTime} seconds")
print(f"Sparse graph with adjacency list: {lazyPrimsSparseListTime} seconds")
print(f"Dense graph with adjacency list: {lazyPrimsDenseListTime} seconds\n")

print(f"Eager Prims Running Times :") 
print(f"\nSparse graph with adjacency matrix: {eagerPrimsSparseMatrixTime} seconds")
print(f"Dense graph with adjacency matrix: {eagerPrimsDenseMatrixTime} seconds")
print(f"Sparse graph with adjacency list: {eagerPrimsSparseListTime} seconds")
print(f"Dense graph with adjacency list: {eagerPrimsDenseListTime} seconds\n")



