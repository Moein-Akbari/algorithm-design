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

section = [None] * n

