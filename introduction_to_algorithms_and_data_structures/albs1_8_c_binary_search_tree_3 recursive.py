# https://www.udemy.com/course/python-algo/learn/lecture/21384630?start=225#overview
from collections import deque


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
            if key == node.key:
                return node
            elif key < node.key:
                return _find(node.left, key)
            elif key > node.key:
                return _find(node.right, key)

        # 内部関数_findで第1引数にrootを指定して呼び出し
        return _find(self.root, key)

    def delete(self, key: int) -> None:
        def _min_node(node: Node) -> Node:
            current_node = node
            # 親ノードより値が小さいノードは必ず左側に存在
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

        def _delete(node: Node, key: int) -> Node:
            # 末尾再帰
            if node == None:
                return None
            # keyの値を持つNodeを再帰で抽出して削除 + 返り値で子の値を更新
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            # keyの値を持つNodeが見つかった時
            # 消去するノードの子ノードを返す
            else:
                delete_node = node
                # 子が一つの場合,その子を返す (孫ノードは存在しない)
                if delete_node.left is None:
                    return delete_node.right
                elif delete_node.right is None:
                    return delete_node.left
                else:
                    # 子が二つの場合,孫ノードまで遡ってその中で最小のノードを返す
                    # ※node.rightの最小を探す理由：消去するノードの代わりに入れる子ノードは、
                    # 　二分木の性質上、左の子ノードよりも値が大きくなければならない
                    min_node = _min_node(delete_node.right)
                    # 消去するノードの代わりの値を最小ノードへ更新
                    delete_node.key = min_node.key
                    # 元々位置していた最小ノードを抽出/削除。子ノードも再帰で更新。
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
