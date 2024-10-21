# In the name of god

from typing import List

def matrix_multipication(dimentions: List[int]) -> int:
    n = len(dimentions)
    minimum_cost = [[0] * (n + 1) for _ in range(n + 1)]
    update_log = minimum_cost.copy()

    for total in range(1, n):
        # print(total)
        for i in range(1, total):
            #TODO: How to move on 
            j = total - i + 1
            # print(i, j)

            minimum = float('+inf')
            for k in range(i, j):
                
                tmp = minimum_cost[i][k] + minimum_cost[k + 1][j]\
                      + dimentions[i - 1] * dimentions[k] * dimentions[j]
                
                if tmp < minimum:
                    minimum = tmp
                    update_log[i][j] = k
            
            minimum_cost[i][j] = minimum

    print(minimum_cost)

    return minimum_cost[1][-2]

if __name__ == '__main__':
    print(matrix_multipication([10, 100, 5, 50]))
    print(matrix_multipication([10, 10, 20, 5, 50]))