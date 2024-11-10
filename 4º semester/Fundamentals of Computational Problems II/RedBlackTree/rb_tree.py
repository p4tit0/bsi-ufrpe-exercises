from .rb_node import Node, Color
from AVLTree.avl_tree import Tree as AVLTree

class Tree(AVLTree):
    
    def __init__(self):
        super(AVLTree, self).__init__()
        self.__nil = Node(None, color=Color.BLACK)
        
        
    def __str__(self) -> str:
        if self.__root is None:
            return "<empty tree>"
        return self._build_ascii_tree(self.__root, "", True)

    def _build_ascii_tree(self, node: Node, prefix: str, is_tail: bool) -> str:
        
        result = ""
        if (node != self.__nil):
            if node.get_right() is not None:
                result += self._build_ascii_tree(node.get_right(), prefix + ("│   " if is_tail else "    "), False)
            
            result += prefix + ("└── " if is_tail else "┌── ") + f"\033[{node.get_color().value}m" + str(node.get_data()) + f"\033[0m\n"
            
            if node.get_left() is not None:
                result += self._build_ascii_tree(node.get_left(), prefix + ("    " if is_tail else "│   "), True)
        
        return result

    def insert(self, node: Node) -> None:
        z = super(AVLTree, self).insert(node)
        node.set_left(self.__nil)
        node.set_right(self.__nil)
        self._rb_insert_fixup(z)
        
    

    def _rb_insert_fixup(self, node: Node) -> None:
        z = node
        while z.get_parent().get_color() == Color.RED:
            if z.get_parent().is_left():
                y = z.get_parent().get_brother()
                if y.get_color() == Color.RED:
                    z.get_parent().set_color(Color.BLACK)
                    y.set_color(Color.BLACK)
                    z.get_parent().get_parent().set_color(Color.RED)
                    z = z.get_parent().get_parent()
                elif z.is_right():
                    z = z.get_parent()
                    super().left_rotate(z)
                else:
                    z.get_parent().set_color(Color.BLACK)
                    z.get_parent().get_parent().set_color(Color.RED)
                    super().right_rotate(z.get_parent().get_parent())
            else:
                y = z.get_parent().get_brother()
                if y.get_color() == Color.RED:
                    z.get_parent().set_color(Color.BLACK)
                    y.set_color(Color.BLACK)
                    z.get_parent().get_parent().set_color(Color.RED)
                    z = z.get_parent().get_parent()
                elif z.is_left():
                    z = z.get_parent()
                    super().right_rotate(z)
                else:
                    z.get_parent().set_color(Color.BLACK)
                    z.get_parent().get_parent().set_color(Color.RED)
                    super().left_rotate(z.get_parent().get_parent())
        self.__root.set_color(Color.BLACK)
        
    def _rb_delete_fixup(self, node: Node) -> None:
        x = node
        while x != self.__root and x.get_color() == Color.BLACK:
            if x.is_left():
                w = x.get_brother()
                if w.get_color() == Color.RED:
                    w.set_color(Color.BLACK)
                    x.get_parent().set_color(Color.RED)
                    super().left_rotate(x.get_parent())
                    w = x.get_parent().get_right()
                if w.get_left().get_color() == Color.BLACK and w.get_right().get_color() == Color.BLACK:
                    w.set_color(Color.RED)
                    x = x.get_parent()
                elif w.get_right().get_color() == Color.BLACK:
                    w.get_left().set_color(Color.BLACK)
                    w.set_color(Color.RED)
                    super().right_rotate(w)
                    w = x.get_parent().get_right()
                else:
                    w.set_color(x.get_parent().get_color())
                    x.get_parent().set_color(Color.BLACK)
                    w.get_right().set_color(Color.BLACK)
                    super().left_rotate(x.get_parent())
                    x = self.__root
            else:
                w = x.get_brother()
                if w.get_color() == Color.RED:
                    w.set_color(Color.BLACK)
                    x.get_parent().set_color(Color.RED)
                    super().right_rotate(x.get_parent())
                    w = x.get_parent().get_left()
                if w.get_right().get_color() == Color.BLACK and w.get_left().get_color() == Color.BLACK:
                    w.set_color(Color.RED)
                    x = x.get_parent()
                elif w.get_left().get_color() == Color.BLACK:
                    w.get_right().set_color(Color.BLACK)
                    w.set_color(Color.RED)
                    super().left_rotate(w)
                    w = x.get_parent().get_left()
                else:
                    w.set_color(x.get_parent().get_color())
                    x.get_parent().set_color(Color.BLACK)
                    w.get_left().set_color(Color.BLACK)
                    super().right_rotate(x.get_parent())
                    x = self.__root
        x.set_color(Color.BLACK)
                    
