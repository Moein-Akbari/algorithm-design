
from pprint import pprint


def minimum_impacts(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = 1
            else:
                low, high = 1, j
                best = j
                while low <= high:
                    mid = (low + high) // 2
                    breaks = dp[i-1][mid-1]
                    no_break = dp[i][j-mid]
                    worst_case = 1 + max(breaks, no_break)
                    
                    # Minimize the worst case
                    best = min(best, worst_case)
                    
                    if breaks > no_break:
                        high = mid - 1
                    else:
                        low = mid + 1
                
                dp[i][j] = best
    
    pprint(dp)
    return dp[n][m]
n = int(input())
m = int(input())
print(minimum_impacts(n, m))