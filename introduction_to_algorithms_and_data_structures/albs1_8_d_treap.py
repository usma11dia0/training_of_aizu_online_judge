from collections import deque
import sys

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.right = None
        self.left = None

class Treap(object):
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key: int, priority: int) -> None:
        if self.root is None:
            self.root = Node(key)
            return

        def _insert(node: Node, key: int) -> Node:
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            # 深さを戻す際は親ノードを返す
            return node
        
        _insert(self.root, key)
      
    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.key)
                _inorder(node.right)
        _inorder(self.root)

    
    def search(self, key: int) -> bool:
        def _search(node: Node, key: int) -> bool:
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            elif key > node.key:
                return _search(node.right, key)
        return _search(self.root, key)

    def min_key(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def remove(self, key: int) -> None:
        def _remove(node: Node, key: int) -> Node:
            if node is None:
                return node
            # 該当のkeyを持つノードを検索
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            # 該当のkeyを持つノードが見つかった場合
            else:
                # 子ノードが一つもない場合、None
                # 子ノードが一つの場合、その子ノードを返す
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # 子ノードが二つの場合
                # 右部分木の最小値ノードを取得
                temp = self.min_key(node.right)
                # 削除するノードの値に最小値ノードの値をコピーして入れ替え
                node.key = temp.key
                # 右部分木から残った最小値ノードを削除
                node.right = _remove(node.right, temp.key)
            return node
        _remove(self.root, key)
         

if __name__ == '__main__':
    treap = Treap()
    treap.insert(35, 99)
    print(treap.search(7))
    treap.remove(6)
    print('************ Remove')
    treap.inorder()
        


