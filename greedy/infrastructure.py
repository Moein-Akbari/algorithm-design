from __future__ import annotations
from functools import total_ordering
from typing import Generic, List, Optional, TypeVar, Union

T = TypeVar('T')


@total_ordering
class BinaryTreeNode(Generic[T]):
    def __init__(
            self, 
            value: Optional[T]=None, 
            right: Optional[BinaryTreeNode[T]]=None,
            left: Optional[BinaryTreeNode[T]]=None
        ) -> None:
        self.value = value
        self.right = right
        self.left = left
    
    def __lt__(self, other: BinaryTreeNode[T]):
        return self.value < other.value
    
    def __eq__(self, other: BinaryTreeNode[T]):
        return self.value == other.value
    
    # fully copied from chatgpt
    def __repr__(self) -> str:
        return f"Node(value={self.value}" + \
               f"{f', left={repr(self.left)}' if self.left else ''}" + \
               f"{f', right={repr(self.right)}' if self.right else ''}" + \
               ")"

    # __str__ gives a "pretty" string representation, showing the tree hierarchy
    def __str__(self) -> str:
        lines = self._tree_str()
        return "\n".join(lines)

    def _tree_str(self, level=0, prefix="Root: ") -> list[str]:
        """
        Helper function to recursively build a list of strings that visually represents the tree.
        """
        lines = []
        lines.append(f"{'  ' * level}{prefix}{self.value}")
        
        if self.left:
            lines.extend(self.left._tree_str(level + 1, prefix="L--- "))
        else:
            lines.append(f"{'  ' * (level + 1)}L--- None")
        
        if self.right:
            lines.extend(self.right._tree_str(level + 1, prefix="R--- "))
        else:
            lines.append(f"{'  ' * (level + 1)}R--- None")
        
        return lines
    

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
