# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7093165#1

# 2分探索木の特徴　参考：アルゴリズム図鑑(アプリ)
# 1. 全てのノードは、そのノードの左部分木に含まれるどの数よりも大きくなる
# 2. 全てのノードは、そのノードの右部分木に含まれるどの数よりも小さくなる

# 2分探索木にてノードを削除する場合
# 子ノードが一つもない場合：そのまま削除
# 子ノードが一つの場合：子ノードを削除ノードの場所へ移し替える
# 子ノードが二つの場合：削除ノードの左部分木から最大ノードを探索し、削除ノードの場所へ移し替える。

from collections import deque
import sys


#二分探索木を実装
class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.right = None
        self.left = None


def insert(node: Node, key: int) -> Node:
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    # 深さを戻す際は親ノードを返す
    return node

def inorder(node: Node) -> None:
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def search(node: Node, key: int) -> bool:
    if node is None:
        return False
    if key == node.key:
        return True
    elif key < node.key:
        return search(node.left, key)
    elif key > node.key:
        return search(node.right, key)

def min_value(node: Node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current

def remove(node: Node, key: int) -> Node:
    if node is None:
        return node
    # 該当のkeyを持つノードを検索
    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
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
        temp = min_value(node.right)
        # 削除するノードの値に最小値ノードの値をコピーして入れ替え
        node.value = temp.value
        # 右部分木から残った最小値ノードを削除
        node.right = remove(node.right, temp.value)
    return node

if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 4)


# class Treap:
#     def __init__(self, root: Node) -> Node:
#         self.root = root

#     def insert(self, z: int) -> None:
#         # zをノード化
#         z = Node(z)
#         # Treapの根
#         root_treap = self.root 
        


