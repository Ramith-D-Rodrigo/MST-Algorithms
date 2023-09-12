import Graph.* 

//create a sparse graph with 10000 vertices
def createSparseGraph(graphType: Int, verticesCount: Int = 10000) : Graph = {
    
    var vertices = (0 until verticesCount).toList;

    var edges = vertices.flatMap(x => 
    vertices.map(y => {
        if(scala.util.Random.nextInt(100000) % 21 == 0){ //random possibiltiy of having an edge
            (x,y,scala.util.Random.nextInt(vertices.length) + 1)
        }
        else{
            (x,y,0)
        }
    }
    )).filter(x => x._3 != 0) //remove edges with weight 0
    .filter(x => {
        if(scala.util.Random.nextInt(50) % 2 == 0){
            x._1 != x._2 && true;   //remove self loop with some random possibility
        }
        else{
            false;
        }
    }); //remove edges with weight 0 and self loops

    return new Graph(graphType, vertices, edges);
}