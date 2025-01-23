from typing import List, Optional


MOD = 10**9 + 7  # Define MOD to avoid errors

# Factorial function
factorial = [1] * 1001 * 1001
for i in range(1, 1001 * 1001):
    factorial[i] = (factorial[i-1] * i) % MOD

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
    return factorial[n] // (factorial[n - k] * factorial[k]) % MOD # Use integer division

# Function to calculate ways with odd edges
def with_odd_ways(n, edges, k):
    possible_edges = choosing(n, 2) - edges  # All possible edges
    ans = choosing(possible_edges, k) * factorial[k]
    return ans % MOD  # Return the result modulo MOD

# Function to calculate ways without odd edges
def without_odd_ways(section1_size, section2_size, edges, k):
    e11 = choosing(section1_size, 2)  # Edges within section1
    e12 = choosing(section2_size, 2)  # Edges within section2_size

    sum_edge_two_sections = e11 + e12  # Total edges within both sections
    edges_between_two_sections = (section1_size) * (section2_size) - edges  # Edges between sections
    ans = 0  # Initialize ans
    for i in range(1, k + 1):  # Iterate from 0 to k
        if i > sum_edge_two_sections:
            break
        if k - i > edges_between_two_sections:
            break
        
        ans += (
            choosing(sum_edge_two_sections, i) * choosing(edges_between_two_sections, k - i) * factorial[k]
        ) % MOD
    return ans % MOD  # Return the result modulo MOD


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
    