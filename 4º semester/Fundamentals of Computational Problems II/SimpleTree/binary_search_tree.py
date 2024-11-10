from .binary_node import Node
from collections.abc import Callable
from typing import Optional

class Tree:
    __root: Node
    __nil: Node
    
    def __init__(self):
        self.__root = None
    
    def is_empty(self):
        return self.__root is None
    
    def set_root(self, node: Node):
        self.__root = node
    
    def get_root(self) -> Node:
        return self.__root

    def __str__(self) -> str:
        if self.__root is None:
            return "<empty tree>"
        return self._build_ascii_tree(self.__root, "", True)

    def _build_ascii_tree(self, node: Node, prefix: str, is_tail: bool) -> str:
        result = ""
        if node.get_right() is not None:
            result += self._build_ascii_tree(node.get_right(), prefix + ("│   " if is_tail else "    "), False)
        
        result += prefix + ("└── " if is_tail else "┌── ") + str(node.get_data()) + "\n"
        
        if node.get_left() is not None:
            result += self._build_ascii_tree(node.get_left(), prefix + ("    " if is_tail else "│   "), True)
        
        return result

    
    @staticmethod
    def pre_order_tree_walk(node: Node, func: Optional[ Callable[[Node], None]] = None) -> Optional[list[Node]]:
        if node is not None:
            result = [node]
            if func is not None:
                func(node)
            result += Tree.pre_order_tree_walk(node.get_left(), func)
            result += Tree.pre_order_tree_walk(node.get_right(), func)
            return result
    
    @staticmethod
    def in_order_tree_walk(node: Node, func: Optional[ Callable[[Node], None]] = None) -> Optional[list[Node]]:
        if node is not None:
            result = []
            result += Tree.pre_order_tree_walk(node.get_left(), func)
            result.append(node)
            if func is not None:
                func(node)
            result += Tree.pre_order_tree_walk(node.get_right(), func)
            return result
    
    @staticmethod
    def post_order_tree_walk(node: Node, func: Optional[ Callable[[Node], None]] = None) -> Optional[list[Node]]:
        if node is not None:
            result = []
            result += Tree.pre_order_tree_walk(node.get_left(), func)
            result += Tree.pre_order_tree_walk(node.get_right(), func)
            result.append(node)
            if func is not None:
                func(node)
            return result
    
    def search(self, node: Node, data: int) -> Optional[Node]:
        if node == self.__nil or data == node.get_data():
            return node
        
        if data < node.get_data():
            return self.search(node.get_left(), data)
        return self.search( node.get_right(), data)
    

    def iterative_search(self, node: Node, data: int) -> Node:
        x = node
        while x != self.__nil and data != x.get_data():
            if data < x.get_data():
                x = x.get_left()
            else:
                x = x.get_right()
        return x
    
    @staticmethod
    def tree_minimum(node: Node) -> Node:
        x = node
        while x.get_left() is not None:
            x = x.get_left()
        return x
    
    @staticmethod
    def tree_maximum(node: Node) -> Node:
        x = node
        while x.get_right() is not None:
            x = x.get_right()
        return x
    
    @staticmethod
    def tree_successor(node: Node) -> Node:
        if node.get_right() is not None:
            return Tree.tree_minimum(node.get_right())
        x = node
        y = x.get_parent()
        while y is not None and x.is_right():
            x = y
            y = y.get_parent()
        return y
    
    @staticmethod
    def tree_predecessor(node: Node) -> Node:
        if node.get_left is not None:
            return Tree.tree_maximum(node.get_left())
        x = node
        y = x.get_parent()
        while y is not None and x == y.get_left():
            x = y
            y = y.get_parent()
        return y
    
    def insert(self, node: Node) -> Node:
        z = node
        y = self.__nil
        x = self.__root
        while x is not None and x != self.__nil:
            y = x
            if z.get_data() < x.get_data():
                x = x.get_left()
            else:
                x = x.get_right()
        z.set_parent(y)
        if y == self.__nil:
            self.set_root(z)
        elif z.get_data() < y.get_data():
            y.set_left(z) 
        else:
            y.set_right(z)
        
        node.set_left(self.__nil)
        node.set_right(self.__nil)
        return z
    
    def delete(self, node: Node):
        y: Node
        if node.get_left() is None or node.get_right() is None:
            y = node
        else:
            y = Tree.tree_successor(node)
        
        x: Node
        if y.get_left() is not None:
            x = y.get_left()
        else:
            x = y.get_right()
        
        if x is not None:
            x.set_parent(y.get_parent) 
        
        if y.get_parent() is None:
            self.__root == x
        
        elif y.is_left(): 
            y.get_parent().set_left(x)
        else:
            y.get_parent().set_right(x)
        
        if y != node:
            node.set_data(y.get_data())
        
        return y