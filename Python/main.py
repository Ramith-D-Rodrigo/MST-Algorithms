from Graph import Graph
from sparseGraphEdges import create_sparse_graph_edges

vertices = [i for i in range(0, 5500)]

edges = create_sparse_graph_edges(vertices)


graph1 = Graph(0, vertices, edges)

graph1.print_graph()