MOD = 10**9 + 7

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % MOD
    return fact

def is_2_sectioned(section, adjacency_list):
    n = len(adjacency_list)
    for i in range(n):
        if section[i] is None:
            section[i] = 0
            stack = [i]
            while stack:
                u = stack.pop(0)
                for v in adjacency_list[u]:
                    if section[v] is None:
                        section[v] = 1 - section[u]
                        stack.append(v)
                    elif section[v] == section[u]:
                        return False
    return True

n, m, k = map(int, input().split())
adjacency_list = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
    
section = [None] * n
two_sectioned = is_2_sectioned(section, adjacency_list)

ans = 0
# print(two_sectioned)
if not two_sectioned:
    total_edges = n * (n - 1) / 2 - m
    ans = factorial(total_edges) / factorial(total_edges - k) % MOD
else:
    same_section = 0
    for u in range(n):
        for v in range(u + 1, n):
            if section[u] == section[v]:
                same_section += 1

    total_edges = n * (n - 1) // 2 - m

    total_ways = factorial(total_edges) // factorial(total_edges - k) % MOD
    invalid_ways = factorial(total_edges - same_section) // factorial(total_edges - same_section - k) % MOD
    
    # print(total_ways)
    # print(invalid_ways)
    ans = (total_ways - invalid_ways) % MOD

    if total_edges - same_section < k:
        ans = total_ways

print(ans)