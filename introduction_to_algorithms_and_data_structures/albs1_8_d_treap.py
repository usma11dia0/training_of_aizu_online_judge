# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7093165#1

from collections import deque


class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.priority = None


class Treap:
    def __init__(self) -> None:
        self.root = None

    def insert(self, z: int):
        z = Node(z)
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key: int) -> Node:
        def _find(node: Node, key: int) -> Node:
            if node == None:
                return None
            if key == node.key:
                return node
            elif key < node.key:
                return _find(node.left, key)
            elif key > node.key:
                return _find(node.right, key)

        return _find(self.root, key)

    def delete(self, key: int) -> None:
        def _min_node(node: Node) -> Node:
            current_node = node
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

        def _delete(node: Node, key: int) -> Node:
            if node == None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                delete_node = node
                if delete_node.left is None:
                    return delete_node.right
                elif delete_node.right is None:
                    return delete_node.left
                else:
                    min_node = _min_node(delete_node.right)
                    delete_node.key = min_node.key
                    node.right = _delete(delete_node.right, min_node.key)
            return node

        _delete(self.root, key)


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
