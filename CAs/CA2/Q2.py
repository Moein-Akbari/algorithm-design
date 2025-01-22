from __future__ import annotations 
from typing import List, Tuple
 
class Node:
    def __init__(self,is_dot:bool,adjs:set[Node]=set()):
        self.is_dot=is_dot
        self.adjs=adjs
    def add_adj(self, other):
        self.adjs.append(other)

n,m,k =list(map(int,input().split())) 
t = []
for _ in range(n):
    t.append(list(input()))

start_points: List[Tuple] = []
for _ in range(k):
    start_points.append(tuple(map(int, input().split())))

#creating Nodes
for i in range(len(t)):
    for j in range(len(t[i])):
        t[i][j]=Node(t[i][j]=='.')#{t[i-1][j],t[i+1][j],t[i][j-1],t[i][j+1]})
for i in range(len(t)):
    for j in range(len(t[i])):
        t[i][j].add_adj(t[i-1][j])
        t[i][j].add_adj(t[i+1][j])
        t[i][j].add_adj(t[i][j-1])
        t[i][j].add_adj(t[i][j+1])








    





    



