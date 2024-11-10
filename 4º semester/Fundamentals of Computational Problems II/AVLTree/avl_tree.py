from .avl_node import Node
from SimpleTree.binary_search_tree import Tree as BinarySearchTree

class Tree(BinarySearchTree):
    
    def __init__(self):
        super().__init__()
        self.__nil = Node(None)

    def get_nil(self):
        return self.__nil()

    def insert(self, node: Node) -> None:
        z = super().insert(node)  
        self._rebalance(z)

    def delete(self, node: Node) -> Node:
        y = super().delete(node)
        if y.get_parent() is not None:
            self._rebalance(y.get_parent())

    def _rebalance(self, node: Node) -> None:
        y: Node
        while node is not None and node != self.__nil:
            self._update_balance(node)
            if node.get_balance() < -1:
                if node.get_left().get_balance() > 0:
                    y = self.left_rotate(node.get_left())
                    self._update_balance(node)
                    self._update_balance(y)

                y = self.right_rotate(node)
                self._update_balance(node)
                self._update_balance(y)
            elif node.get_balance() > 1:
                if node.get_right().get_balance() < 0:
                    y = self.right_rotate(node.get_right())
                    self._update_balance(node)
                    self._update_balance(y)
                y = self.left_rotate(node)
                self._update_balance(node)
                self._update_balance(y)
            node = node.get_parent()

    def _update_balance(self, node: Node) -> None:
        if node is None:
            return
        node.set_balance(self._height(node.get_right()) - self._height(node.get_left()))

    def _height(self, node: Node) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.get_left()), self._height(node.get_right()))

    def left_rotate(self, node: Node) -> Node:
        y = node.get_right()
        node.set_right(y.get_left())
        if y.get_left() is not None:
            y.get_left().set_parent(node)
        y.set_parent(node.get_parent())
        if node.get_parent() is None:
            self.set_root(y)
        elif node.is_left():
            node.get_parent().set_left(y)
        else:
            node.get_parent().set_right(y)
        y.set_left(node)
        node.set_parent(y)
        
        return y
        
    def right_rotate(self, node: Node) -> Node:
        y = node.get_left()
        node.set_left(y.get_right())
        if y.get_right() is not None:
            y.get_right().set_parent(node)
        y.set_parent(node.get_parent())
        if node.get_parent() is None:
            self.set_root(y)
        elif node.is_right():
            node.get_parent().set_right(y)
        else:
            node.get_parent().set_left(y)
        y.set_right(node)
        node.set_parent(y)
        
        
        return y