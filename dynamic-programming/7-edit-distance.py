# In the name of God
# https://www.geeksforgeeks.org/edit-distance-dp-5/

import pprint
from enum import Enum
from typing import List, Tuple


class Operations(Enum):
    NO_OPERATION = 1
    REMOVE = 2
    INSERT = 3
    MUTATE = 4

    def __repr__(self) -> str:
        return self.name


def get_previous_cell(i: int, j: int, operation: Operations) -> Tuple[int, int]:
    match operation:
        case Operations.NO_OPERATION:
            return (i - 1, j - 1)
        case Operations.REMOVE:
            return (i, j - 1)
        case Operations.INSERT:
            return (i - 1, j)
        case Operations.MUTATE:
            return (i - 1, j - 1)


def minimum_operations_for_conversion(dna: str, pattern: str) \
        -> Tuple[List[Tuple[int, Operations]], int]:
    m = len(dna) + 1
    n = len(pattern) + 1
    minimum_operations = [[float("+inf")] * m for _ in range(n)]
    chosen_operation = [[None] * m for _ in range(n)]
    minimum_operations[0] = list(range(m))
    for i in range(n):
        minimum_operations[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            # NoOp
            if pattern[i - 1] == dna[j - 1]:
                if minimum_operations[i - 1][j - 1] < minimum_operations[i][j]:
                    minimum_operations[i][j] = minimum_operations[i - 1][j - 1]
                    chosen_operation[i][j] = Operations.NO_OPERATION

            # Remove
            if minimum_operations[i][j - 1] + 1 < minimum_operations[i][j]:
                minimum_operations[i][j] = minimum_operations[i][j - 1] + 1
                chosen_operation[i][j] = Operations.REMOVE

            # Insert
            if minimum_operations[i - 1][j] + 1 < minimum_operations[i][j]:
                minimum_operations[i][j] = minimum_operations[i - 1][j] + 1
                chosen_operation[i][j] = Operations.INSERT

            # Mutate
            if minimum_operations[i - 1][j - 1] + 1 < minimum_operations[i][j]:
                minimum_operations[i][j] = minimum_operations[i - 1][j - 1] + 1
                chosen_operation[i][j] = Operations.MUTATE
    # pprint.pprint(minimum_operations)

    operations: List[Operations] = []
    i, j = n - 1, m - 1
    while i != 0 or j != 0:
        prev_i, prev_j = get_previous_cell(i, j, chosen_operation[i][j])
        operations.append((j, chosen_operation[i][j]))
        i, j = prev_i, prev_j
    operations.reverse()
    # pprint.pprint(chosen_operation)

    return operations, minimum_operations[-1][-1]


if __name__ == '__main__':
    pprint.pprint(minimum_operations_for_conversion('ACTCAATG', 'AGCTAAA'))
