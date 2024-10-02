
from typing import Generic, List, TypeVar

T = TypeVar('T')

class MinHeap(Generic[T]):
    def __init__(self, data: List[T] = []) -> None:
        self.__data: List[T] = []
        # All we need to know is that 
        if data:
            self.__heapify(data)


    def __len__(self) -> int:
        return len(self.__data)


    def push(self, node: T) -> None:
        self.__data.append(node)
        self.__bubble_up(-1)


    def pop(self) -> T:
        pass


    def peek(self) -> T:
        pass

    
    def __get_parent_index(self, index: int) -> int:
        return int((index - 1) / 2)
    
    def __get_left_child(self, index: int) -> int:
        return index * 2 + 1
    
    def __get_right_child(self, index: int) -> int:
        return index * 2 + 2

    def __heapify(self, data: List[T]) -> None:
        raise NotImplementedError()
    
    def __bubble_up(self, index: int):
        parent_index = self.__get_parent_index(index)

        while self.__data[index] < self.__data[parent_index]:
            self.__data[index] 


    def __bubble_down(self, index: int):
        pass

