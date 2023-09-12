import Kruskal.*
import Graph.* 

object KruskalAccuracyTest extends App{

    var vertices = (0 to 9).toList; //10 vertices

    var edges = vertices.flatMap(x => 
        vertices.map(y => {
            if(scala.util.Random.nextInt(100) % 7 == 0){ //random possibiltiy of having an edge
                (x,y,scala.util.Random.nextInt(10) + 1)
            }
            else{
                (x,y,0)
            }
        }
        )).filter(x => x._3 != 0 && x._1 != x._2); //remove edges with weight 0 and self loops

    for(i <- edges){
        println(i.toString());
    }

    var matrixGraph = new Graph(0, vertices, edges);

    var listGraph = new Graph(1, vertices, edges);

    var kruskalMatrix = new Kruskal(matrixGraph);

    var kruskalList = new Kruskal(listGraph);

    println("Kruskal MST using matrix Graph");

    kruskalMatrix.printMinimumSpanningTree();

    println("Kruskal MST using list Graph");

    kruskalMatrix.printMinimumSpanningTree();
}