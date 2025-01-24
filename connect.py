vertices = []
edges = {}
def connect():
    for vertices, cost in edges.items():
        v1, v2 = vertices









while True:
    vertix_count, edge_count = [int(_) for _ in input().strip().split()]

    if vertix_count == 0 or edge_count == 0:
        break

    for edge in range(edge_count):
        v1, v2, cost = [int(_) for _ in input().strip().split()]

        if {v1} not in vertices:
            vertices.append({v1})

        if {v2} not in vertices:
            vertices.append({v2})

        edges[(v1, v2)] = cost

    edges = dict(sorted(edges.items(), key=lambda item: item[1]))

    print(edges)



