import pprint
from typing import List, Set, Tuple


def relax(u, v, w, distances, parents):
    if distances[v] > distances[u] + w:
        distances[v] = distances[u] + w
        parents[v] = u


def bellman_ford(
    edges: List[Tuple[int, int, int]], vertices: Set[int]
) -> Tuple[List[float], List[int]]:
    parents = [None] * len(vertices)
    distances = [float('+inf')] * len(vertices) 
    distances[0] = 0

    for _ in range(len(vertices) - 1):
        for edge in edges:
            relax(*edge, distances, parents)

    return distances, parents


def print_path(vertex, parents):
    if parents[vertex] is None:
        print(vertex)
    else:
        print_path(parents[vertex], parents)
        print(vertex)

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

    distances, parents = bellman_ford(edges, vertices)

    for vertex in vertices:
        print(f'Vertex: {vertex}')
        print(f'Distance: {distances[vertex]}')
        print('Path:')
        print_path(vertex, parents)
        print()