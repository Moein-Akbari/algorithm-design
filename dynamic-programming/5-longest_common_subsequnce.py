from typing import List, Tuple


def longest_common_subsequence(str1, str2) -> Tuple[int, str]:
    n = len(str1) + 1
    m = len(str2) + 1
    lcs = [[0] * m for _ in range(n)]
    
    update_log = [[None] * (len(str2) + 1) for i in range(len(str1) + 1)]
    
    for i, char1 in enumerate(str1, 1):
        for j, char2 in enumerate(str2, 1):
            if char1 == char2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
                update_log[i][j] = (i - 1, j - 1)
            else:
                if lcs[i][j - 1] < lcs[i - 1][j]:
                    lcs[i][j] = lcs[i - 1][j]
                    update_log[i][j] = (i - 1, j)
                else:
                    lcs[i][j] = lcs[i][j - 1]
                    update_log[i][j] = (i, j - 1)

    answer: List[str] = []
    prev_i, prev_j = (n - 1, m - 1)
    while len(answer) < lcs[-1][-1]:
        next_i, next_j = update_log[prev_i][prev_j]
        if lcs[next_i][next_j] < lcs[prev_i][prev_j]:
            answer.append(str1[prev_i - 1])
        prev_i, prev_j = next_i, next_j

    return lcs[-1][-1], ''.join(answer[::-1])


if __name__ == '__main__':
    print(longest_common_subsequence('abcde', 'ace'))
    print(longest_common_subsequence('CTCCGATAC', 'CAAGTCTT'))
    # [
    #     [None, None, None, None], 
    #     [None, (0, 0), (1, 1), (1, 2)], 
    #     [None, +(1, 1), (2, 1), (2, 2)], 
    #     [None, (2, 1), -(2, 1), (3, 2)], 
    #     [None, (3, 1), *(3, 2), (4, 2)], 
    #     [None, (4, 1), (4, 2), (4, 2)]
    # ]
    # [
    #     [0, 0, 0, 0], 
    #     [0, 1, 0, 0], 
    #     [0, +1, 0, 0], 
    #     [0, 1, -2, 0], 
    #     [0, 1, *2, 0], 
    #     [0, 1, 2, 3]
    # ]