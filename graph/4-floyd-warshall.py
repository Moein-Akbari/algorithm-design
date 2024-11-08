# in the name of God

import pprint
from typing import List, Set, Tuple


def floyd_warshall(
    edges: List[Tuple[int, int, int]], vertices: Set[int]
) -> Tuple[List[float], List[int]]:
    distance = [[float('+inf')] * len(vertices) for _ in range(len(vertices))]  

    for edge in edges:
        distance[edge[0]][edge[1]] = edge[2]
    
    for vertex in vertices:
        distance[vertex][vertex] = 0

    # pprint.pprint(distance)

    for middle_vertex in range(len(vertices)):
        for source_vertex in range(len(vertices)):
            for destination_vertex in range(len(vertices)):
                distance[source_vertex][destination_vertex] = min(
                    distance[source_vertex][destination_vertex],
                    distance[source_vertex][middle_vertex] + distance[middle_vertex][destination_vertex]
                )

    return distance

if __name__ == "__main__":
    edges = [
        (0, 1, 6),
        (0, 4, 7),
        
        (1, 2, 5),
        (1, 3, -4),
        (1, 4, 8),

        (2, 1, -2),

        (3, 0, 2),
        (3, 2, 7),

        (4, 3, 9),
        (4, 2, -3),
    ]

    vertices = {edge[0] for edge in edges} | {edge[1] for edge in edges}

    distance = floyd_warshall(edges, vertices)

    pprint.pprint(distance)