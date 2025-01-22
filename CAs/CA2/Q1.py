MOD = 10**9 + 7

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % MOD
    return fact

def is_bipartite(n, adj):
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        return False, color
    return True, color

def count_valid_ways(n, m, k, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    bipartite, color = is_bipartite(n, adj)
    
    if not bipartite:
        # The graph is already non-bipartite, any edge addition is valid
        total_edges = n * (n - 1) // 2 - m
        return pow(total_edges, k, MOD)
    
    # The graph is bipartite, we need to add at least one edge within the same partition
    # Count the number of edges that can be added within the same partition
    count_same_partition = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if color[u] == color[v]:
                count_same_partition += 1
    
    # Total edges that can be added
    total_edges = n * (n - 1) // 2 - m
    
    # The number of ways to add k edges such that at least one is within the same partition
    # Total ways = total_edges^k - (total_edges - count_same_partition)^k
    total_ways = pow(total_edges, k, MOD)
    invalid_ways = pow(total_edges - count_same_partition, k, MOD)
    valid_ways = (total_ways - invalid_ways) % MOD
    
    return valid_ways

# Read input
n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Compute and print the result
print(count_valid_ways(n, m, k, edges))