# https://www.udemy.com/course/python-algo/learn/lecture/21384630?start=225#overview


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
                return -1
            # keyの値を持つNodeを再帰で抽出
            if node.key == key:
                return Node
            elif node.key > key:
                return _find(node.left, key)
            elif node.key < key:
                return _find(node.right, key)

        # 内部関数_findで第1引数にrootを指定して呼び出し
        return _find(self.root, key)

    def delete(self, key: int) -> None:

        # 木からkeyのNodeを探す。
        target_node = self.find(key)

        # 子を一つも持たない場合
        if target_node.left == None and target_node.right == None:
            return None
        
        # 子を一つのみ持つ場合
        elif target_node.left == None or target_node.right == None:
            pass

        pass


# 探索順を全て出力
def print_order_all(T: BinarySearchTree) -> None:

    # 深さ優先探索(先行順巡回)
    def _print_preorder(T: BinarySearchTree, node: Node):
        print(f" {node.key}", end="")
        if node.left != None:
            _print_preorder(T, node.left)
        if node.right != None:
            _print_preorder(T, node.right)

    # 深さ優先探索(中間順巡回)
    def _print_inorder(T: BinarySearchTree, node: Node) -> None:
        if node.left != None:
            _print_inorder(T, node.left)
        print(f" {node.key}", end="")
        if node.right != None:
            _print_inorder(T, node.right)

    # 結果の出力
    _print_inorder(T, T.root)
    print()
    _print_preorder(T, T.root)
    print()


m = int(input())
command_list = [list(input().split()) for _ in range(0, m)]

T = BinarySearchTree()

for command in command_list:
    if command[0] == "insert":
        T.insert(int(command[1]))
    elif command[0] == "find":
        is_find = T.find(int(command[1]))
        if is_find:
            print("yes")
        else:
            print("no")
    elif command[0] == "print":
        print_order_all(T)
