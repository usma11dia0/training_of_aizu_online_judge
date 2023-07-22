# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7093165#1

# 2分探索木の特徴　参考：アルゴリズム図鑑(アプリ)
# 1. 全てのノードは、そのノードの左部分木に含まれるどの数よりも大きくなる
# 2. 全てのノードは、そのノードの右部分木に含まれるどの数よりも小さくなる

# 2分探査木にてノードを削除する場合
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

class Treap:
    def __init__(self, root: Node) -> Node:
        self.root = root

    def insert(self, z: int) -> None:
        # zをノード化
        z = Node(z)
        # Treapの根
        root_treap = self.root 
        


