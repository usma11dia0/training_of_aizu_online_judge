from collections import deque
import sys

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.right = None
        self.left = None

class Treap:
    def __init__(self, root: Node) -> Node:
        self.root = root

    def insert(self, z: int) -> None:
        # zをノード化
        z = Node(z)
        # Treapの根
        root_treap = self.root 

        # 大小を比較しながらleftまたはrightがNoneとなる子まで移動し、
        # その親を取得
        while root_treap != None:
            y = root_treap


        # 大小を比較しながらleftまたはrightがNoneとなる子まで移動し、
        # その親を取得
        while root_treap != None:
            y = root_treap



