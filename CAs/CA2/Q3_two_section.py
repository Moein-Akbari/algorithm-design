from typing import List, Optional

MOD = 10**9 + 7

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % MOD
    return fact

n, m, k = map(int, input().split())
adjacency_list = [[] for _ in range(n)]


for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)



def two_section(adjacency_list) -> Optional[List[int]]:
    sections = [None] * len(adjacency_list)
    sections[0] = 0
    queue = [0]

    while queue:
        u = queue.pop(0)
        for v in adjacency_list[u]:
            if sections[v] is None:
                sections[v] = 1 - sections[u] # Toggle
                queue.append(v)
            elif sections[v] == sections[u]:
                return None

    return sections

print(two_section(adjacency_list))