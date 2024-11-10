from __future__ import annotations
from SimpleTree.binary_node import Node as BinarySearchNode

class Node(BinarySearchNode):
    __balance_factor: int
    
    def __init__(self, data, left_child: Node = None, right_child: Node = None, parent: Node = None) -> None:
        super().__init__(data, left_child, right_child, parent)
        self.__balance_factor = 0      
    
    def set_balance(self, new_balance) -> None:
        self.__balance_factor = new_balance
        
    def get_balance(self) -> int:
        return self.__balance_factor