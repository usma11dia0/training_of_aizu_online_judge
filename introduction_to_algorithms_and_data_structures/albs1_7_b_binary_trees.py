# https://aotamasaki.hatenablog.com/entry/2019/11/03/%E8%9E%BA%E6%97%8B%E6%9C%AC%E3%82%92Python%E3%81%A7%E8%A7%A3%E3%81%8F_Part2

# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_preorder/print.html
# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_inorder/print.html
# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_postorder/print.html


class Node:
    def __init__(
        self,
        parent: int,
        sibling: int,
        degree: int,
        depth: int,
        height: int,
        type: str,
        left: int,
        right: int,
    ):
        self.parent = parent
        self.sibling = sibling
        self.degree = degree
        self.depth = depth
        self.height = height
        self.type = type
        self.left = left
        self.right = right


# 深さ優先探索にて二分木の深さを導出
def get_depth(T: dict, u: int, p: int):
    T[u].depth = p
    if T[u].left != -1:
        get_depth(T, T[u].left, p + 1)
    if T[u].right != -1:
        get_depth(T, T[u].right, p + 1)


# 深さ優先探索にて二分木の高さを導出
def get_height(T: dict, u: int):
    # 初期値の設定。末尾再帰にて利用。
    h_left, h_right = 0, 0
    if T[u].left != -1:
        h_left = get_height(T, T[u].left) + 1
    if T[u].right != -1:
        h_right = get_height(T, T[u].right) + 1
    height = max(h_left, h_right)
    T[u].height = height
    return height


def print_result(T: dict) -> None:
    for i in range(len(T)):
        output = f"node {i}: "
        output += f"parent = {T[i].parent}, "
        output += f"sibling = {T[i].sibling}, "
        output += f"degree = {T[i].degree}, "
        output += f"depth = {T[i].depth}, "
        output += f"height = {T[i].height}, "
        output += f"{T[i].type}"
        print(output)


n = int(input())

# キーを節点番号, 値をNodeとした辞書を生成
T = {i: Node(-1, -1, 0, 0, 0, "", -1, -1) for i in range(0, n)}

# T内のNodeへ入力データから得られる情報を追記
for _ in range(0, n):
    node_info = list(map(int, input().split()))

    # ノード_info[0]に対する処理
    # 子ノードの追記
    T[node_info[0]].left = node_info[1]
    T[node_info[0]].right = node_info[2]

    # 次数, 節点の種類の追記
    if T[node_info[0]].left != -1 and T[node_info[0]].right != -1:
        T[node_info[0]].degree = 2
        T[node_info[0]].type = "internal node"
    elif T[node_info[0]].left != -1 or T[node_info[0]].right != -1:
        T[node_info[0]].degree = 1
        T[node_info[0]].type = "internal node"
    else:
        T[node_info[0]].degree = 0
        T[node_info[0]].type = "leaf"

    # ノード_info[0]の子に対する処理
    # 親ノードの追記
    if T[node_info[0]].left != -1:
        T[node_info[1]].parent = node_info[0]
    if T[node_info[0]].right != -1:
        T[node_info[2]].parent = node_info[0]

    # 兄弟の追記
    if T[node_info[0]].left != -1 and T[node_info[0]].right != -1:
        T[node_info[1]].sibling = node_info[2]
        T[node_info[2]].sibling = node_info[1]

# rootの探索・追記
for k, v in T.items():
    if v.parent == -1:
        root = k
        break
T[root].type = "root"

# 深さの導出
get_depth(T, root, 0)

# 高さの導出
get_height(T, root)

# 結果の出力
print_result(T)
