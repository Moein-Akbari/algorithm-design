# Internal
from typing import List, Tuple
import heapq

# Local
from infrastructure.BinaryTree import Node


def huffman_coding(alphabet_frequencies: List[Tuple[str, int]]) -> Tuple[str, int]:
    heap_data = [Node((freq, char)) for char, freq in alphabet_frequencies]
    heapq.heapify(heap_data)

    for _ in range(len(alphabet_frequencies) - 1):
        z = Node()
        x = heapq.heappop(heap_data)
        y = heapq.heappop(heap_data)

        z.left = x if x < y else y
        z.right = x if x >= y else y

        z.value = (x.value[0] + y.value[0], None)
        heapq.heappush(heap_data, z)

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