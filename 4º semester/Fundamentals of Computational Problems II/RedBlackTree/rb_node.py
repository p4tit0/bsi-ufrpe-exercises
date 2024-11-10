from __future__ import annotations
from SimpleTree.binary_node import Node as BinaryNode
from enum import Enum

class Color(Enum):
    BLACK = 30
    RED = 31
    

class Node(BinaryNode):
    __color: Color
    
    def __init__(self, data, left_child: Node = None, right_child: Node = None, parent: Node = None, color: Color = Color.RED) -> None:
        super().__init__(data, left_child, right_child, parent)
        self.__color = color      
    
    def set_color(self, new_color: Color) -> None:
        self.__color = new_color
        
    def get_color(self) -> Color:
        return self.__color