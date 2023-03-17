# https://www.udemy.com/course/python-algo/learn/lecture/21384630?start=225#overview
from collections import deque
import sys


class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, z: int):
        # zをノード化
        z = Node(z)
        # xの親
        y = None
        # Tの根
        x = self.root

        # 大小を比較しながらleftまたはrightがNoneとなる子まで移動し、
        # その親を取得
        while x != None:
            # 親を設定
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        # Tが空の時
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key: int) -> Node:
        def _find(node: Node, key: int) -> Node:
            # 末尾再帰
            if node == None:
                return None
            # keyの値を持つNodeを再帰で抽出
            if node.key == key:
                return node
            elif node.key > key:
                return _find(node.left, key)
            elif node.key < key:
                return _find(node.right, key)

        # 内部関数_findで第1引数にrootを指定して呼び出し
        return _find(self.root, key)

    def delete(self, key: int) -> None:

        # 木からkeyのNodeを探す。
        # z : 削除対象のノード
        z = self.find(key)

        if self.root.key == z.key:
            self.root = None

        # 子を一つも持たない場合
        if z.left == None and z.right == None:
            if z.parent.left == z:
                z.parent.left = None
            else:
                z.parent.right = None

        # 子を一つのみ持つ場合
        # 削除対象zの左側の子がない場合：
        elif z.left == None:
            # 削除対象zが親の左側の子である場合：
            if z.parent.left == z:
                z.parent.left = z.right
                z.right.parent = z.parent.left
            # 削除対象zが親の右側の子である場合：
            else:
                z.parent.right = z.right
                z.right.parent = z.parent
        # 削除対象zの右側の子がない場合：
        elif z.right == None:
            if z.parent.left == z:
                z.parent.left = z.left
                z.left.parent = z.parent
            else:
                z.parent.right = z.left
                z.left.parent = z.parent

        # 子を二つ持つ場合
        else:
            # 削除対象ノードの右部分木の最小ノードを見つける
            target_node = z.right
            while target_node.left != None:
                target_node = target_node.left

            # 削除対象ノードと右部分木の最小ノードを入れ替え
            z.key = target_node.key

            # 上記でzの位置に移動したため、不要な最小ノードを削除
            if target_node.parent.left == target_node:
                # 最小ノードの親の新たな子として、新たに設定するのは最小ノードの右側のみ。
                # (左側の子が存在した場合、その子が最小ノードになるため)
                target_node.parent.left = target_node.right
            else:
                target_node.parent.right = target_node.right

            if target_node.right != None:
                target_node.right.parent = target_node.parent


# 深さ優先探索(リスト生成)
def preorder(node: Node, queue: deque) -> list:
    if node.left != None:
        preorder(node.left, queue)
    queue.append(node)
    if node.right != None:
        preorder(node.right, queue)


# 探索順を全て出力
def print_order_all(T: BinarySearchTree) -> None:
    # 深さ優先探索(先行順巡回)
    def _print_preorder(node: Node) -> None:
        print(f" {node.key}", end="")
        if node.left != None:
            _print_preorder(node.left)
        if node.right != None:
            _print_preorder(node.right)

    # 深さ優先探索(中間順巡回)
    def _print_inorder(node: Node) -> None:
        if node.left != None:
            _print_inorder(node.left)
        print(f" {node.key}", end="")
        if node.right != None:
            _print_inorder(node.right)

    # 結果の出力
    _print_inorder(T.root)
    print()
    _print_preorder(T.root)
    print()


m = int(input())
command_list = [list(input().split()) for _ in range(0, m)]

T = BinarySearchTree()

for command in command_list:
    if command[0] == "insert":
        T.insert(int(command[1]))
    elif command[0] == "find":
        if T.find(int(command[1])) != None:
            print("yes")
        else:
            print("no")
    elif command[0] == "delete":
        T.delete(int(command[1]))
    elif command[0] == "print":
        print_order_all(T)
