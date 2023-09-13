package graph

//create a dense graph edges
def createDenseGraphEdges(vertices : Array[Int]) : Array[(Int, Int, Int)] = {
    
    return vertices.flatMap(x => 
    vertices.map(y => {
        (x,y,scala.util.Random.nextInt(vertices.length) + 1) //no randomness in dense graph
    }
    )).toArray;

}