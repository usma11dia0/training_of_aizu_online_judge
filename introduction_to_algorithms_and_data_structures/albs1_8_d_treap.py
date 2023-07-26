from collections import deque
import sys

class Node:
    def __init__(self, key: int, priority: int) -> None:
        self.key = key
        self.priority = priority
        self.right = None
        self.left = None

class Treap:
    def __init__(self) -> None:
        self.root = None
    
    def _right_rotate(self, old_root: Node) -> Node:
        # 対象部分木のrootを入れ替え
        new_root = old_root.left
        # old_rootの左子ノードにnew_rootの右子ノードを挿入
        # ※二分探索木の条件を満たすため
        old_root.left = new_root.right
        # new_rootの右子ノードにold_rootを挿入
        new_root.right = old_root
        return new_root
    
    def _left_rotate(self, old_root: Node) -> Node:
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left = old_root
        return new_root

    def insert(self, key: int, priority: int) -> None:
        if self.root is None:
            self.root = Node(key, priority)
            return
        def _insert(node: Node, key:int, priority: int) -> None:
            # 再帰終了条件
            # 子ノードがない時に挿入位置確定
            if node is None:
                return Node(key, priority)
            if key < node.key:
                node.left = _insert(node.left, key, priority)
                # 左の子の方が優先度が高い場合、右回転
                if node.priority < node.left.priority:
                    pass     
            else:
                node.right = _insert(node.right, key, priority)
            # 深さを戻す際に親ノードを返す
            return node
    
        _insert(self.root, key, priority)

if __name__ == '__main__':
    treap = Treap()
    treap.insert(35, 99)
    treap.insert(3, 80)






