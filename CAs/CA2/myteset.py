MOD = 10**9 + 7  # Define MOD to avoid errors

# Factorial function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % MOD
    return fact

# Choosing function (n choose k)
def choosing(n, k):
    if k > n or k < 0:
        return 0
    return factorial(n) // factorial(n - k) * factorial(k) % MOD # Use integer division

# Function to calculate ways with odd edges
def with_odd_ways(n, edges, k):
    possible_edges = choosing(n, 2) - edges  # All possible edges
    ans = choosing(possible_edges, k) * factorial(k)
    return ans % MOD  # Return the result modulo MOD

# Function to calculate ways without odd edges
def without_odd_ways(section1, section2, edges, k):
    e11 = choosing(len(section1), 2)  # Edges within section1
    e22 = choosing(len(section2), 2)  # Edges within section2
    #we know that for this two sectiono we don't have any edge yet
    sum_edge_two_sections = e11 + e22  # Total edges within both sections
    edges_between_two_sections = len(section1) * len(section2) - edges  # Edges between sections
    ans = 0  # Initialize ans
    for i in range(1,k ):  # Iterate from 0 to k
        ans += choosing(sum_edge_two_sections, i) * choosing(edges_between_two_sections, k - i) * factorial(k)
    return ans % MOD  # Return the result modulo MOD

# Example usage
if __name__ == "__main__":
    n = 5  # Total number of vertices
    edges = 3  # Number of existing edges
    k = 2  # Number of edges to choose
    section1 = [1, 2, 3]  # Define section1
    section2 = [4, 5]  # Define section2

    # Calculate ways
    ways_with_odd = withodd_ways(n, edges, k)
    ways_without_odd = withoutodd_ways(section1, section2, edges, k)

    print("Ways with odd edges:", ways_with_odd)
    print("Ways without odd edges:", ways_without_odd)