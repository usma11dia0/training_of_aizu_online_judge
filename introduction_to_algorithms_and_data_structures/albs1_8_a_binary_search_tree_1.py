class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.p = None


class binary_search_tree:
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


# 探索順を全て出力
def print_order_all(T: binary_search_tree) -> None:
    def _print_preorder(T: binary_search_tree, u: Node):
        print(f" {u.key}", end="")
        if u.left != None:
            _print_preorder(T, u.left)
        if u.right != None:
            _print_preorder(T, u.right)

    # 深さ優先探索(中間順巡回)
    def _print_inorder(T: binary_search_tree, u: Node) -> None:
        if u.left != None:
            _print_inorder(T, u.left)
        print(f" {u.key}", end="")
        if u.right != None:
            _print_inorder(T, u.right)

    # 結果の出力
    _print_inorder(T, T.root)
    print()
    _print_preorder(T, T.root)
    print()


m = int(input())
command_list = [list(input().split()) for _ in range(0, m)]

T = binary_search_tree()

for command in command_list:
    if command[0] == "insert":
        T.insert(int(command[1]))
    elif command[0] == "print":
        print_order_all(T)
