from typing import Generic, List, TypeVar

T = TypeVar('T')

class MinHeap(Generic[T]):
    def __init__(self, data: List[T] = []) -> None:
        self.__data: List[T] = []
        if data:
            self.__heapify(data)
    
    def __len__(self) -> int:
        return len(self.__data)


    def push(self, node: T) -> None:
        pass


    def pop(self) -> T:
        pass


    def peek(self) -> T:
        pass

        
    def __heapify(self, data: List[T]) -> None:
        raise NotImplementedError()
    
    def __bubble_up(self, index: int):
        pass

    def __bubble_down(self, index: int):
        pass