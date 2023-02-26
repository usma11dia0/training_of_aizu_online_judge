# https://aotamasaki.hatenablog.com/entry/2019/11/03/%E8%9E%BA%E6%97%8B%E6%9C%AC%E3%82%92Python%E3%81%A7%E8%A7%A3%E3%81%8F_Part2

# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_preorder/print.html
# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_inorder/print.html
# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_postorder/print.html


class Node:
    def __init__(
        self,
        id: int,
        parent: int,
        left: int,
        right: int,
    ):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right


# 深さ優先探索(先行順巡回)
def print_preorder(T: dict, u: int):
    print(f" {T[u].id}", end="")
    if T[u].left != -1:
        print_preorder(T, T[u].left)
    if T[u].right != -1:
        print_preorder(T, T[u].right)


# 深さ優先探索(中間順巡回)
def print_inorder(T: dict, u: int):
    if T[u].left != -1:
        print_inorder(T, T[u].left)
    print(f" {T[u].id}", end="")
    if T[u].right != -1:
        print_inorder(T, T[u].right)


# 深さ優先探索(後行順巡回)
def print_postorder(T: dict, u: int):
    if T[u].left != -1:
        print_postorder(T, T[u].left)
    if T[u].right != -1:
        print_postorder(T, T[u].right)
    print(f" {T[u].id}", end="")


n = int(input())

# キーを節点番号, 値をNodeとした辞書を生成
T = {i: Node(-1, -1, -1, -1) for i in range(0, n)}

# T内のNodeへ入力データから得られる情報を追記
for _ in range(0, n):
    node_info = list(map(int, input().split()))

    # ノード_info[0]に対する処理
    T[node_info[0]].id = node_info[0]
    # 子ノードの追記
    T[node_info[0]].left = node_info[1]
    T[node_info[0]].right = node_info[2]

    # ノード_info[0]の子に対する処理
    # 親ノードの追記
    if T[node_info[0]].left != -1:
        T[node_info[1]].parent = node_info[0]
    if T[node_info[0]].right != -1:
        T[node_info[2]].parent = node_info[0]

# rootの探索・追記
for k, v in T.items():
    if v.parent == -1:
        root = k
        break
T[root].type = "root"


# 結果の出力
print("Preorder")
print_preorder(T, root)
print()
print("Inorder")
print_inorder(T, root)
print()
print("Postorder")
print_postorder(T, root)
print()
