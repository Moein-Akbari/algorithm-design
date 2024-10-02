# Internal
from typing import Generic, List, Tuple, TypeVar
import heapq

# External
from binarytree import Node # https://pypi.org/project/binarytree/


def huffman_coding(alphabet_frequencies: List[Tuple[str, int]]) -> Tuple[str, int]:
    heap_data = [(freq, char) for char, freq in alphabet_frequencies]
    heapq.heapify(heap_data)

    for _ in range(len(alphabet_frequencies) - 1):
        x = heapq.heappop(heap_data)
        y = heapq.heappop(heap_data)
        heapq.heappush(heap_data, (x[0] + y[0], None))

    return heap_data

if __name__ == '__main__':
    print(huffman_coding([
            ('a', 45),
            ('b', 13),
            ('c', 12),
            ('d', 16),
            ('e', 9),
            ('f', 5)
    ]))