package union_find

class UnionFind(vertexList: Array[Int]) {
    var parent: Array[Int] = new Array[Int](vertexList.length);

    for (i <- 0 until vertexList.length) {   //initialize parent array
        parent(i) = i;
    }

    def find(x: Int): Int = {
        if (parent(x) == x) {
            return x;
        }
        else {
            return find(parent(x));
        }
    }

    def union(x: Int, y: Int): Unit = {
        parent(find(y)) = find(x);
    }
}