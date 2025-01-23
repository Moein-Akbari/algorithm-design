from typing import List, Optional

MOD = 10**9 + 7  # Define MOD to avoid errors

# Factorial function
factorial = [1] * (1001 * 1001)
for i in range(1, 1001 * 1001):
    factorial[i] = (factorial[i-1] * i) % MOD

# Inverse factorial function
inv_fact = [1] * (1001 * 1001)
inv_fact[1001 * 1001 - 1] = pow(factorial[1001 * 1001 - 1], MOD - 2, MOD)
for i in range(1001 * 1001 - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

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

def choosing(n, k):
    # Choosing function (n choose k)
    if k > n or k < 0:
        return 0
    return (factorial[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD

# Function to calculate ways with odd edges
def with_odd_ways(n, edges, k):
    possible_edges = (n * (n - 1) // 2) - edges  # All possible edges
    ans = choosing(possible_edges, k) * factorial[k] % MOD
    return ans  # Return the result modulo MOD

# Function to calculate ways without odd edges
def without_odd_ways(section1_size, section2_size, edges, k):
    e11 = choosing(section1_size, 2)  # Edges within section1
    e12 = choosing(section2_size, 2)  # Edges within section2_size

    sum_edge_two_sections = (e11 + e12) % MOD  # Total edges within both sections
    edges_between_two_sections = (section1_size * section2_size) - edges  # Edges between sections
    ans = 0  # Initialize ans
    for i in range(1, k + 1):  # Iterate from 0 to k
        if i > sum_edge_two_sections:
            break
        if k - i > edges_between_two_sections:
            continue
        
        ans = (ans + choosing(sum_edge_two_sections, i) * choosing(edges_between_two_sections, k - i) % MOD * factorial[k]) % MOD
    return ans  # Return the result modulo MOD

n, m, k = map(int, input().split())
adjacency_list = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

sections = two_section(adjacency_list)
if sections is None:
    print(with_odd_ways(n, m, k))
else:
    section1_size = sum(sections)
    section2_size = len(sections) - section1_size
    print(without_odd_ways(section1_size, section2_size, m, k))