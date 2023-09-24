import kruskal.Kruskal
import graph.*

object KruskalEfficiency extends App{
    //sparse graph
    var vertices = (0 until 5500).toArray;
    println("Created vertices");

    var sparseEdges = createSparseGraphEdges(vertices);
    println("Created sparse edges");

    var sparseMatrixGraph = new Graph(0, vertices, sparseEdges);
    println("Created sparse matrix graph")

    var sparseListGraph = new Graph(1, vertices, sparseEdges);
    println("Created sparse list graph")

    //start time to calculate time taken by Kruskal's algorithm using matrix representation
    println("Creating kruskal MST for matrix representation");
    var sparseMatrixStartTime = System.nanoTime();
    var sparseKruskalMatrix = new Kruskal(sparseMatrixGraph);
    //end time to calculate time taken by Kruskal's algorithm using matrix representation
    var sparseMatrixEndTime = System.nanoTime();


    //start time to calculate time taken by Kruskal's algorithm using list representation
    println("Creating kruskal MST for list representation");
    var sparseListStartTime = System.nanoTime();
    var sparseKruskalList = new Kruskal(sparseListGraph);
    //end time to calculate time taken by Kruskal's algorithm using list representation
    var sparseListEndTime = System.nanoTime();


    println("Sparse Graph Matrix Representation Kruskal MST time : " + (sparseMatrixEndTime - sparseMatrixStartTime) / 1000000);
    println("Sparse Graph List Representation Kruskal MST time : " + (sparseListEndTime - sparseListStartTime) / 1000000);

}