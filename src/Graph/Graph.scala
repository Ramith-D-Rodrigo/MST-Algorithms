package Graph

class Graph(graphType: Int, vertexList: List[Int], edgeList: List[(Int, Int, Int)]){    //edgeList -> (src, dest, weight)
    var adjacencyMatrix: Array[Array[Int]] = null;
    var adjacencyList: Array[List[(Int, Int)]] = null; //dest, weight

    graphType match {
        case 0 => { //adjacency matrix
            //create a 2d array of size vertexList.length x vertexList.length
            adjacencyMatrix = Array.ofDim[Int](vertexList.length, vertexList.length);

            //initialize adjacency matrix
            for(i <- 0 until vertexList.length){
                for(j <- 0 until vertexList.length){
                    adjacencyMatrix(i)(j) = Int.MaxValue;   //infinity
                }
            }

            //populate adjacency matrix with edgeList
            for(i <- 0 until edgeList.length){
                adjacencyMatrix(edgeList(i)._1)(edgeList(i)._2) = edgeList(i)._3;
                adjacencyMatrix(edgeList(i)._2)(edgeList(i)._1) = edgeList(i)._3;
            }
        }

        case 1 => { //adjacency list
            //create a list of size vertexList.length
            adjacencyList = Array.ofDim[List[(Int, Int)]](vertexList.length);

            //initialize adjacency list
            for(i <- 0 until vertexList.length){
                adjacencyList(i) = List();
            }

            //populate adjacency list with edgeList
            for(i <- 0 until edgeList.length){
                adjacencyList(edgeList(i)._1) = (edgeList(i)._2, edgeList(i)._3) :: adjacencyList(edgeList(i)._1);
                adjacencyList(edgeList(i)._2) = (edgeList(i)._1, edgeList(i)._3) :: adjacencyList(edgeList(i)._2);
            }
        }

        case _ => {
            println("Invalid graph type.");
        }
    }

    def getGraphType() : Int = {
        return graphType;
    }

    def printGraph(): Unit = {
        graphType match{
            case 0 => { //adjacency matrix
                for(i <- 0 until vertexList.length){
                    for(j <- 0 until vertexList.length){
                        print(adjacencyMatrix(i)(j) + " ");
                    }
                    println();
                }
            }

            case 1 => { //adjacency list
                for(i <- 0 until vertexList.length){
                    print(i + ": ");
                    for(j <- 0 until adjacencyList(i).length){
                        print("(" + adjacencyList(i)(j)._1 + "," + adjacencyList(i)(j)._2 + ") ");
                    }
                    println();
                }
            }

            case _ => {
                println("Invalid graph type.");
            }
        }
    }

    def getEdgeCount() : Int = {
        return edgeList.length;
    }

}