import random

def create_sparse_graph_edges(vertices):
    edges = []

    for x in vertices:
        for y in vertices:
            if x == y:  # no self loops
                edges.append((x, y, 0))
                continue
            
            if random.randint(0, 100000) % 71 == 0:  # Random possibility of having an edge
                edges.append((x, y, random.randint(1, int(len(vertices) / 4))))


    return edges