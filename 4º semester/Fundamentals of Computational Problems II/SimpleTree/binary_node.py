from __future__ import annotations


class Node:
    __data: int
    __left_child: Node
    __right_child: Node
    __parent: Node
    
    def __init__(self, data, left_child: Node = None, right_child: Node = None, parent: Node = None) -> None:
        self.__data = data
        self.__left_child = left_child
        self.__right_child = right_child
        self.__parent = parent
    
    
    def set_data(self, new_data: int) -> None:
        self.__data = new_data
    
    def set_left(self, new_left_child: Node) -> None:
        self.__left_child = new_left_child
        
    def set_right(self, new_right_child: Node) -> None:
        self.__right_child = new_right_child
        
    def set_parent(self, new_parent: Node) -> None:
        self.__parent = new_parent
    
    def get_data(self) -> int:
        return self.__data
    
    def get_left(self) -> Node:
        return self.__left_child
    
    def get_right(self) -> Node:
        return self.__right_child
    
    def get_parent(self) -> Node:
        return self.__parent
    
    def is_left(self) -> bool:
        return self.get_parent().get_left() == self
    
    def is_right(self) -> bool:
        return self.get_parent().get_right() == self
    
    def get_brother(self) -> Node:
        if self.is_left():
            return self.get_parent().get_right()
        return self.get_parent().get_left()
    
    
                
        


    