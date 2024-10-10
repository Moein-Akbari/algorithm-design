# in the name of God

from typing import Tuple

def find_number_of_paths(n, m, obstacles: set[Tuple[int, int]]):
    number_of_ways = [[0] * n for _ in range(m)]

    for i in range(n):
        number_of_ways[i][0] = 1
    
    for j in range(m):
        number_of_ways[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if (i, j) not in obstacles:
                # print(i, j)
                number_of_ways[i][j] = number_of_ways[i - 1][j] + number_of_ways[i][j - 1] 

    return number_of_ways[-1][-1]

if __name__ == '__main__':
    tst1 = [(1, 1)]
    print(find_number_of_paths(3, 3, tst1))