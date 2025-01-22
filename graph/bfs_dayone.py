
from __future__ import annotations  

weight=[]
class Node:
    def __init__(self, _id, _adj:list[Node]=None ):
        self.id=_id
        self.color='white'
        self.pi=None
        self.d=float('inf')
        self.adj=[]
    @staticmethod    
    def add_edge( v:Node,u:Node,weight_value:float):
        v.adj.append(u)
        
        u.adj.append(v)
        weight.append((v,u,weight_value ))
    @staticmethod
    def w(u:Node,v:Node):
        for i in  range(len(weight)):
            if weight[i][0]==u and weight[i][1]==v:
                return weight[i][2]
            else:
                print('you dont have a weight  for this vertices ')

class graph:
    @staticmethod
    def createGraph (weight :list[(Node , Node, float)])->list:
        edges=[]
        for vertex in weight:
            edges.append(vertex)
            return edges
    @staticmethod      
    def printGraph(edges):
        i=0
        for edge in edges:
            print(f" {edge[i][0].id} and {edge[i][1].id} have { edge[i][2]}")
            i=+1



        

if __name__ == '__main__':
    a1=Node('a')
    a2=Node('b')
    a3=Node('c')
    a4=Node('d')
    a5=Node('e')
    a6=Node('f')
    a7=Node('g')
    a8=Node('h')
    a9=Node('i')
    Node.add_edge(a1,a2,4)
    Node.add_edge(a1,a8,8)
    Node.add_edge(a2,a3,8)
    Node.add_edge(a3,a4,7)
    Node.add_edge(a4,a5,9)
    Node.add_edge(a5,a6,10)
    Node.add_edge(a6,a7,2)
    Node.add_edge(a7,a8,1)
    Node.add_edge(a8,a9,7)
    Node.add_edge(a9,a7,6)
    Node.add_edge(a9,a3,2)
    Node.add_edge(a4,a6,14)
    print(Node.w(a4,a6))
    print(weight)
    e=graph.createGraph(weight)
    graph.printGraph(e)
#how to change multiple line simuntanesly shift +-> or <- + ctrl + alt |^ or |