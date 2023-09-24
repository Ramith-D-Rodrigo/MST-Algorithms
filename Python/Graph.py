class Graph:
    def __init__(self, graph_type, vertex_list, edge_list):
        self.adjacency_matrix = None
        self.adjacency_list = None  # dest, weight

        if graph_type == 0:  # adjacency matrix
            # create a 2D list of size len(vertex_list) x len(vertex_list)
            vertex_len = len(vertex_list)
            self.adjacency_matrix = [[float('inf')] * vertex_len for _ in range(vertex_len)]

            # initialize adjacency matrix
            #for i in range(vertex_len):
                ##for j in range(vertex_len):
                    ##self.adjacency_matrix[i][j] = float('inf')

            # populate adjacency matrix with edge_list
            for i in range(len(edge_list)):
                self.adjacency_matrix[edge_list[i][0]][edge_list[i][1]] = edge_list[i][2]
                self.adjacency_matrix[edge_list[i][1]][edge_list[i][0]] = edge_list[i][2]

        elif graph_type == 1:  # adjacency list
            # create a list of size len(vertex_list)
            self.adjacency_list = [[] for _ in range(len(vertex_list))]

            # populate adjacency list with edge_list
            for i in range(len(edge_list)):
                self.adjacency_list[edge_list[i][0]].append((edge_list[i][1], edge_list[i][2]))
                self.adjacency_list[edge_list[i][1]].append((edge_list[i][0], edge_list[i][2]))

        else:
            print("Invalid graph type.")

    def get_graph_type(self):
        return self.graph_type

    def print_graph(self):
        if self.adjacency_matrix is not None:  # adjacency matrix
            for row in self.adjacency_matrix:
                print("\t".join(str(weight) if weight != float('inf') else "-" for weight in row))
        elif self.adjacency_list is not None:  # adjacency list
            for i, adjacency in enumerate(self.adjacency_list):
                print(f"{i}: " + " ".join(f"({dest},{weight})" for dest, weight in adjacency))
        else:
            print("Invalid graph type.")

    def get_edge_count(self):
        return len(self.edge_list)