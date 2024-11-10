from RedBlackTree.rb_tree import Tree
from RedBlackTree.rb_node import Node
import random

def generate_random_list(size: int) -> list[int]:
    """
    Generates a list of random integers between 0 and 10.

    :param size: The number of elements in the list.
    :return: A list of random integers.
    """
    return [random.randint(0, size) for _ in range(size)]

def main():
    size = 10
    random_numbers = generate_random_list(size)
    print(f"Generated list of {size} random numbers between 0 and 10: {', '.join(str(x) for x in random_numbers)}")
    
    tree = Tree()
    for number in random_numbers:
        tree.insert(Node(number))
    
        
    print(tree)

if __name__ == "__main__":
    main()