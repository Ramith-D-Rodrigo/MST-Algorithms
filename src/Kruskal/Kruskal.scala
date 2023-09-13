package kruskal

import graph.Graph
import union_find.UnionFind
import scala.collection.mutable.Set as SET

class Kruskal(graph: Graph){

    var minimumSpanningTree  = SET[(Int, Int, Int)]();

    graph.getGraphType() match {
        case 0 => { //adjacency matrix
            var unionFind = new UnionFind((0 until graph.adjacencyMatrix.length).toArray);

/*             for(i <- unionFind.parent){
                println(i);
            } */
            
            var orderedEdgeList = graph.adjacencyMatrix.zipWithIndex.flatMap{
                                        case (row, x) => (row.zipWithIndex.map{case (value, y) => (x, y, value)})   //first flat map to get the indices and edge weight
                                    }
                                    .sortWith((x, y) => x._3 < y._3)    //sort the edges in increading order
                                    .filter((x) => x._3 != Int.MaxValue);   //remove the infinity (unreachable edge links)

/*             for(i <- orderedEdgeList){
                println(i);
            } */

            createMST(orderedEdgeList, unionFind);
        }


        case 1 => { //adjacency list
            var unionFind = new UnionFind((0 until graph.adjacencyList.length).toArray);

            var orderedEdgeList = graph.adjacencyList.zipWithIndex.flatMap{
                            case (edgeList, x) => (edgeList.map(listItem => (x, listItem._1, listItem._2)))   //first flat map to get the indices and edge weight
                        }
                        .sortWith((x, y) => x._3 < y._3)    //sort the edges in increading order
                        //no need to filter

            createMST(orderedEdgeList, unionFind);
        }

    }

    def createMST(orderedEdgeList: Array[(Int, Int, Int)], unionFindStructure: UnionFind) : Unit = {
        for(i <- orderedEdgeList){
            if(unionFindStructure.find(i._1) != unionFindStructure.find(i._2)){
                minimumSpanningTree = minimumSpanningTree.union(SET((i._1, i._2, i._3)));
                minimumSpanningTree = minimumSpanningTree.union(SET((i._2, i._1, i._3)));

                unionFindStructure.union(unionFindStructure.find(i._1), unionFindStructure.find(i._2));
            }
        }
    }

    def printMinimumSpanningTree() : Unit = {
        for(i <- minimumSpanningTree.toList){
            println(i);
        }
    }
/*     var unionFind = UnionFind(graph);

    //sorting the edges
    var orderedEdgeList = graph.edgeList.sortWith((x, y) => x._3 < y._3);   

    for(i <- 0 until orderedEdgeList.length){
        if(unionFind.find(orderedEdgeList(i)._1) != unionFind.find(orderedEdgeList(i)._2)){

        }
    } */
}