import random

def create_sparse_graph_edges(vertices):
    edges = []

    for x in vertices:
        for y in vertices:
            if random.randint(0, 100000) % 21 == 0:  # Random possibility of having an edge
                edges.append((x, y, random.randint(1, len(vertices))))
            else:
                edges.append((x, y, 0))

    # Filter out edges with weight 0 and self-loops with some random possibility
    edges = [(x, y, weight) for x, y, weight in edges if weight != 0 and (x != y or random.randint(0, 100000) % 2 == 0)]

    return edges