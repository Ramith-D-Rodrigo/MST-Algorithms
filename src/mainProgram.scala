import Kruskal.*
import Graph.Graph

object mainProgram extends App{

    var vertices = (0 to 10).toList;

    var edges = List((1,2,3),(1,3,4),(1,4,3),(2,3,2),(2,4,7),(3,4,1),(3,5,6));

    var graph = new Graph(1, vertices, edges);

    graph.printGraph();

    var kruskal = new Kruskal(graph);

    kruskal.printMinimumSpanningTree();

}