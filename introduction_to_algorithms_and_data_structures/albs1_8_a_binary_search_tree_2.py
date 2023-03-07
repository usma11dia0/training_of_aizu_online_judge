class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.p = None


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
        z.p = y

        # Tが空の時
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key: int) -> bool:
        def _find(node: Node, key: int) -> bool:
            if node == None:
                return False
            if node.key == key:
                return True
            elif node.key > key:
                return _find(node.left, key)
            elif node.key < key:
                return _find(node.right, key)

        return _find(self.root, key)


# 探索順を全て出力
def print_order_all(T: BinarySearchTree) -> None:
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
