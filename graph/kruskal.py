from __future__ import annotations
import pprint
class disjointSet:
    def __init__(self,_id) -> None:
        self.parent = None
        self.rank = 0
        self.id = _id
    def get_parent(self):
        if self.parent == None:
            # print(self.id)
            return self
        # print(self.parent.id)
        self.parent = self.parent.get_parent()
        return self.parent
    @staticmethod    
    def union(set1:disjointSet, set2:disjointSet):
        parent1 = set1.get_parent()
        parent2 = set2.get_parent()
        if parent1.rank < parent2.rank:
            parent1.parent = parent2
        elif parent1.rank > parent2.rank:
            parent2.parent = parent1   
        elif parent1.rank == parent2.rank:
            parent1.parent = parent2
            parent2.rank += 1

if __name__ == '__main__':
    edges = [
        [0, 1 ,4],
        [0, 7, 8],
        [1, 7, 11],
        [1, 2, 8],
        [7, 8, 7],
        [7, 6, 1],
        [8, 6, 6],
        [8, 2, 2],
        [6, 5, 2],
        [5, 2, 4],
        [5, 3, 14],
        [5, 4, 10],
        [2, 3, 7],
        [3, 4, 9],
    ]
    connected_components = dict()
    sum_edges = 0
    selected_edges = []
    vertices = {edge[0] for edge in edges} | {edge[1] for edge in edges}
    print(vertices)
    for vertex in vertices:
        connected_components[vertex] = disjointSet(vertex)


    sorted_edges = sorted(edges, key=lambda x : x[2])
    for edge in sorted_edges:
        u, v = edge[0:2]
        parent_u = connected_components[u].get_parent()
        parent_v = connected_components[v].get_parent()
        if parent_u == parent_v:
            continue
        disjointSet.union(connected_components[u], connected_components[v])
        selected_edges.append(edge)
        sum_edges += edge[2]
    pprint.pprint(selected_edges)
    print(sum_edges)   