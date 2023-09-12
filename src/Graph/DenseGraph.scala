import Graph.* 

//create a dense graph with 10000 vertices
def createDenseGraph(graphType: Int, verticesCount: Int = 10000) : Graph = {
    
    var vertices = (0 until verticesCount).toList;

    var edges = vertices.flatMap(x => 
    vertices.map(y => {
        (x,y,scala.util.Random.nextInt(vertices.length) + 1) //no randomness in dense graph
    }
    ));

    return new Graph(graphType, vertices, edges);
}