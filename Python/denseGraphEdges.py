import random

def create_dense_graph_edges(vertices):
    edges = []

    for x in vertices:
        for y in vertices:
            if x == y:  # no self loops
                edges.append((x, y, 0))
                continue
            edges.append((x, y, random.randint(1, int(len(vertices) / 4))))

    return edges