package graph

//create a sparse graph edges
def createSparseGraphEdges(vertices: Array[Int]): Array[(Int, Int, Int)] = {

    return vertices.flatMap(x => 
    vertices.map(y => {
        if(scala.util.Random.nextInt(100000) % 21 == 0){ //random possibiltiy of having an edge
            (x,y,scala.util.Random.nextInt(vertices.length) + 1)
        }
        else{
            (x,y,0)
        }
    }
    )).filter(x => {
        if(x._3 == 0){  //remove edges with weight 0
            false;
        }

        //remove self loop with some random possibility
        if(x._1 == x._2){
            if(scala.util.Random.nextInt(100000) % 2 == 0){
                false;
            }
            else{
                true;
            }
        }
        else{
            true;
        }
    }).toArray; //remove edges with weight 0 and self loops
}