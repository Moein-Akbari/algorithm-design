
class Node:
    def __init__(self,_id,neighbor:list[tuple])->None:
        self.id= _id
        self.color= "white"
        self.adj=[]
        n=len(neighbor)
        for i in range(n):
            self.adj.append(neighbor[i])
            #print(self.adj)

class graph:
    def __init__ (self , _nodes:list[Node]) :
            self.nodes=[]
            x=len(_nodes)
            for i in range (x):
                self.nodes.append(_nodes[i]) 
    def print_my_graph(self):
         for node in self.nodes:
              
              print(f"my node is  {node.id} and  it neighbor are :  ")
              for vertices in node.adj:
                   print(f"{vertices[0]} with weight {vertices[1]} ")

def DFS_search(node:Node, visited:list[Node], g:graph):
     node.color="black"
     for node in node.adj:
          id_of_my_node=node[0]
          for where_is in g.nodes:
               if where_is.id == id_of_my_node:
                    new_node=where_is
          if new_node.color!='black':
           visited.append(new_node)
           print(f" i have seen node {new_node.id}")
           DFS_search(new_node, visited , g)

g=graph([Node('a',[('b',3),('c',3)]), Node('b',[('c',5),('d',4)]), Node('c',[('d',7)]),  Node('d',[('b',2)])])

g.print_my_graph()
MyFirstNode=g.nodes[0]#the type is node !

visited=[]
DFS_search(MyFirstNode,visited,g)
print('finish!!! visited are ')
print(visited)