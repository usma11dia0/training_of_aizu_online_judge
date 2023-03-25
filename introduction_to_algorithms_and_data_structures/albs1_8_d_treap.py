# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7093165#1

from collections import deque


class Node:
    def __init__(self, key: int, priority: int) -> None:
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None


class Treap:
    def __init__(self) -> None:
        self.root = None

    def _rightRotate(self, t: Node) -> Node:
        s = Node(None, None)
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def _leftRotate(self, t: Node) -> Node:
        s = Node(None, None)
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, key: int, priority: int) -> None:
        def _insert(node: Node, key: int, priority: int) -> Node:
            if node == None:
                return Node(key, priority)
            if key == node.key:
                return node

            if key < node.key:
                node.left = _insert(node.left, key, priority)
                if node.priority < node.left.priority:
                    node = self._rightRotate(node)
            else:
                node.right = _insert(node.right, key, priority)
                if node.priority < node.right.priority:
                    node = self._leftRotate(node)
            return node

        self.root = _insert(self.root, key, priority)

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
                if delete_node.left is None and delete_node.right is None:
                    return None
                elif delete_node.left is None:
                    delete_node = self._leftRotate(delete_node)
                elif delete_node.right is None:
                    delete_node = self._rightRotate(delete_node)
                else:
                    if delete_node.left.priority > delete_node.right.priority:
                        delete_node = self._rightRotate(delete_node)
                    else:
                        delete_node = self._leftRotate(delete_node)
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
def print_order_all(T: Treap) -> None:
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

T = Treap()

for command in command_list:
    if command[0] == "insert":
        T.insert(int(command[1]), int(command[2]))
    elif command[0] == "find":
        if T.find(int(command[1])) != None:
            print("yes")
        else:
            print("no")
    elif command[0] == "delete":
        T.delete(int(command[1]))
    elif command[0] == "print":
        print_order_all(T)
