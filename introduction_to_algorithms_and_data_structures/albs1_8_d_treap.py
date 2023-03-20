class Node:
    def __init__(self, key: int, left: int, right: int, parent: int) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree:
    def __init__(self, root: int):
        self.root = root
