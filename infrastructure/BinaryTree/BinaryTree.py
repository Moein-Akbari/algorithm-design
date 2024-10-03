from __future__ import annotations
from functools import total_ordering
from typing import Generic, List, Optional, TypeVar, Union

T = TypeVar('T')

@total_ordering
class Node(Generic[T]):
    def __init__(
            self, 
            value: Optional[T]=None, 
            right: Optional[Node[T]]=None,
            left: Optional[Node[T]]=None
        ) -> None:
        self.value = value
        self.right = right
        self.left = left
    
    def __lt__(self, other: Node[T]):
        return self.value < other.value
    
    def __eq__(self, other: Node[T]):
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