from typing import List

def matrix_multipication(dimentions: List[int]) -> int:
    minimum_cost = [[0] * len(dimentions) for _ in range(len(dimentions))]
    # update_log = minimum_cost.copy()

    for total in range(1, len(dimentions)):
        for i in range(0, total):
            #TODO: How to move on 
            j = total - i + 1
            
            minimum = float('+inf')
            for k in range(i, j - 1):
                
                minimum = min(
                    minimum, 
                    minimum_cost[i][k]
                    + minimum_cost[k + 1][j] 
                    + dimentions[i - 1] * dimentions[k] * dimentions[j]
                )

    return minimum_cost[0][-1]

if __name__ == '__main__':
    print(matrix_multipication([10, 100, 5, 50]))