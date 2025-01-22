from __future__ import annotations  # Required for forward references in type hints

weight = []


class Node:
    def __init__(self, _id, _adj: list[Node] = None):
        self.id = _id
        self.color = 'white'
        self.pi = None
        self.d = float('inf')
        self.adj = []

    def __repr__(self):#__repr__ and __str__ helps you to print anyything which is related to your class 
        return f"Node({self.id})"

    @staticmethod
    def add_edge(v: Node, u: Node, weight_value: float):
        v.adj.append(u)
        # If it is not directed:
        u.adj.append(v)
        weight.append((v, u, weight_value))

    @staticmethod
    def w(u: Node, v: Node):
        for i in range(len(weight)):
            if weight[i][0] == u and weight[i][1] == v:
                return weight[i][2]
        print('You don\'t have a weight for these vertices.')


class Graph:
    @staticmethod
    def createGraph(weight: list[(Node, Node, float)]) -> list:
        edges = []
        for vertex in weight:
            edges.append(vertex)
        return edges

    @staticmethod
    def printGraph(edges):
        for edge in edges:
            u, v, w = edge  # Unpack the tuple
            print(f"{u.id} and {v.id} have weight {w}")
            # I can use this insted of the previous one because I have a repr method 
            # print(f"{u} and {v} have weight {w}")


if __name__ == '__main__':
    a1 = Node('a')
    a2 = Node('b')
    a3 = Node('c')
    a4 = Node('d')
    a5 = Node('e')
    a6 = Node('f')
    a7 = Node('g')
    a8 = Node('h')
    a9 = Node('i')

    Node.add_edge(a1, a2, 4)
    Node.add_edge(a1, a8, 8)
    Node.add_edge(a2, a3, 8)
    Node.add_edge(a3, a4, 7)
    Node.add_edge(a4, a5, 9)
    Node.add_edge(a5, a6, 10)
    Node.add_edge(a6, a7, 2)
    Node.add_edge(a7, a8, 1)
    Node.add_edge(a8, a9, 7)
    Node.add_edge(a9, a7, 6)
    Node.add_edge(a9, a3, 2)
    Node.add_edge(a4, a6, 14)

    print(Node.w(a4, a6))  # Prints the weight of the edge between a4 and a6
    print(weight)          # Prints the list of edges with weights

    edges = Graph.createGraph(weight)
    Graph.printGraph(edges)  # Prints the edges in a readable format

